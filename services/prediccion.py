# service.py
from sqlalchemy.orm import Session
from sqlalchemy import text
import numpy as np
from sklearn.linear_model import LinearRegression

def predecir_ventas_producto(db: Session, producto_id: int, meses_a_predecir: int = 3):
    # 1. Extraer datos históricos (últimos 3 años agrupados por mes)
    query = text("""
        SELECT 
            DATE_TRUNC('month', ped.created_at) AS mes,
            SUM(dp.cantidad)::INTEGER AS total_ventas
        FROM pedidos ped
        JOIN detalle_pedidos dp ON ped.id = dp.pedido_id
        WHERE dp.producto_id = :producto_id
          AND ped.created_at >= CURRENT_DATE - INTERVAL '3 months'
          AND ped.estado != 'cancelado'
        GROUP BY mes
        ORDER BY mes ASC;
    """)
    
    resultados = db.execute(query, {"producto_id": producto_id}).mappings().all()
    
    # Validación: Si el producto es nuevo y no tiene historial suficiente
    if len(resultados) < 3:
        return {"error": "Datos históricos insuficientes para realizar una regresión (mínimo 3 meses)."}

    # 2. Preparar los datos para el modelo
    # X = El tiempo (mes 0, mes 1, mes 2...)
    # y = La cantidad de ventas en ese mes
    X_historico = np.array(range(len(resultados))).reshape(-1, 1)
    y_historico = np.array([row["total_ventas"] for row in resultados])

    # 3. Entrenar el modelo de Regresión Lineal
    modelo = LinearRegression()
    modelo.fit(X_historico, y_historico)

    # 4. Realizar la predicción para los próximos N meses
    ultimo_mes_index = len(resultados) - 1
    X_futuro = np.array([ultimo_mes_index + i for i in range(1, meses_a_predecir + 1)]).reshape(-1, 1)
    
    predicciones = modelo.predict(X_futuro)

    # 5. Formatear la respuesta
    # (Aseguramos que no devuelva ventas negativas, lo cual matemáticamente 
    # puede pasar en regresiones de productos en declive)
    ventas_proyectadas = [max(0, int(round(p))) for p in predicciones]

    return {
        "producto_id": producto_id,
        "historico_meses_analizados": len(resultados),
        "tendencia": "creciente" if modelo.coef_[0] > 0 else "decreciente",
        "coeficiente_crecimiento": round(modelo.coef_[0], 2), # Cuántas ventas extra suma cada mes
        "prediccion_proximos_meses": ventas_proyectadas
    }