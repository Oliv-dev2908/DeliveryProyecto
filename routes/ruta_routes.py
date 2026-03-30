from fastapi import APIRouter
from controllers.ruta_controller import ruta_optimizada_controller

router = APIRouter()

@router.post("/rutas/optimizar")
def optimizar_ruta(body: dict):

    return ruta_optimizada_controller(body)