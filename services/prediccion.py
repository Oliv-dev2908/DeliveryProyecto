# service.py
from sqlalchemy.orm import Session
from sqlalchemy import text
import numpy as np
from sklearn.linear_model import LinearRegression

def predecir_ventas_producto(db: Session, producto_id: int, meses_a_predecir: int = 3):
    # Generamos el calendario de 4 meses (el actual y los 3 anteriores)
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

    return {
        "producto_id": producto_id,
        "historico_meses_analizados": len(resultados),
        "ventas_historicas": ventas_pasadas, # <-- Aquí se devuelven los meses analizados
        "tendencia": "creciente" if modelo.coef_[0] > 0 else "decreciente",
        "coeficiente_crecimiento": round(modelo.coef_[0], 2),
        "prediccion_proximos_meses": ventas_proyectadas
    }