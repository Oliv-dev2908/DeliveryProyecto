# service.py
from sqlalchemy.orm import Session
from sqlalchemy import text
import numpy as np
from sklearn.linear_model import LinearRegression

def predecir_ventas_producto(db: Session, producto_id: int, meses_a_predecir: int = 3):
    # 1. Obtenemos el precio unitario del producto para calcular el ingreso monetario
    precio_query = text("SELECT precio_unitario FROM productos WHERE id = :producto_id")
    precio_resultado = db.execute(precio_query, {"producto_id": producto_id}).scalar()
    
    # Si el producto no existe, cortamos la ejecución
    if precio_resultado is None:
        return {"error": f"No se encontró el producto con ID {producto_id}."}
        
    precio_unitario = float(precio_resultado)

    # 2. Generamos el calendario de 4 meses (el actual y los 3 anteriores)
    query = text("""
        WITH meses AS (
            SELECT generate_series(
                DATE_TRUNC('month', CURRENT_DATE - INTERVAL '3 months'), 
                DATE_TRUNC('month', CURRENT_DATE),
                INTERVAL '1 month'
            )::DATE AS mes_base
        ),
        ventas_agrupadas AS (
            SELECT 
                DATE_TRUNC('month', ped.created_at)::DATE AS mes_venta,
                SUM(dp.cantidad)::INTEGER AS total_vendido
            FROM pedidos ped
            JOIN detalle_pedidos dp ON ped.id = dp.pedido_id
            WHERE dp.producto_id = :producto_id
              AND ped.estado != 'cancelado'
            GROUP BY DATE_TRUNC('month', ped.created_at)
        )
        SELECT 
            m.mes_base AS mes,
            COALESCE(v.total_vendido, 0) AS total_ventas
        FROM meses m
        LEFT JOIN ventas_agrupadas v ON m.mes_base = v.mes_venta
        ORDER BY m.mes_base ASC;
    """)
    
    resultados = db.execute(query, {"producto_id": producto_id}).mappings().all()
    
    if len(resultados) < 3:
        return {"error": "Datos históricos insuficientes para realizar una regresión (mínimo 3 meses)."}

    # Extraemos las ventas
    y_historico = np.array([row["total_ventas"] for row in resultados])
    X_historico = np.array(range(len(resultados))).reshape(-1, 1)

    # Entrenamos el modelo
    modelo = LinearRegression()
    modelo.fit(X_historico, y_historico)

    # Predecimos el futuro
    ultimo_mes_index = len(resultados) - 1
    X_futuro = np.array([ultimo_mes_index + i for i in range(1, meses_a_predecir + 1)]).reshape(-1, 1)
    
    predicciones = modelo.predict(X_futuro)
    ventas_proyectadas = [max(0, int(round(p))) for p in predicciones]

    # Convertimos el numpy array a una lista normal de Python
    ventas_pasadas = y_historico.tolist()

    # 3. Calculamos la ganancia multiplicando la predicción por el precio
    ganancia_estimada = [round(cantidad * precio_unitario, 2) for cantidad in ventas_proyectadas]

    return {
        "producto_id": producto_id,
        "precio_unitario_actual": precio_unitario,
        "historico_meses_analizados": len(resultados),
        "ventas_historicas_cantidades": ventas_pasadas, 
        "tendencia": "creciente" if modelo.coef_[0] > 0 else "decreciente",
        "coeficiente_crecimiento": round(modelo.coef_[0], 2),
        "prediccion_proximos_meses_cantidades": ventas_proyectadas,
        "prediccion_proximos_meses_ganancias": ganancia_estimada # <-- Aquí agregamos el dato financiero
    }