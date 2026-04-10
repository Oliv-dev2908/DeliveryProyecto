from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.producto_routes import router as producto_router
from routes.categoria_routes import router as categoria_router
from routes.pedido_routes import router as pedido_router
from routes.ubicacion_routes import router as ubicacion_router
from routes.ruta_routes import router as ruta_router
from routes.detalle_pedido_routes import router as detalle_pedido_routes


app = FastAPI()

app.include_router(auth_router)
app.include_router(producto_router)
app.include_router(categoria_router)
app.include_router(pedido_router)
app.include_router(ubicacion_router)
app.include_router(ruta_router)
app.include_router(detalle_pedido_routes)