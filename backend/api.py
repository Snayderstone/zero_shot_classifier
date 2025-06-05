from fastapi import APIRouter, HTTPException, status, Request  # Importa FastAPI Router, manejo de excepciones, códigos de estado y Request
from .schemas import Message, MessageResponse  # Importa los esquemas de entrada y salida definidos en schemas.py
from .model import classify_message  # Importa la función que realiza la clasificación del mensaje
from .logger import logger  # Importa el logger personalizado para registrar eventos

router = APIRouter()  # Crea un router para definir rutas específicas de la API

@router.get("/", tags=["Root"])
def root():
    """
    Endpoint raíz para verificar que la API está activa.
    """
    return {"message": "Zero-Shot Message Classifier API está levantada y lista para recibir peticiones."}

@router.post(
    "/clasificar/",  # Ruta del endpoint
    response_model=MessageResponse,  # Esquema de respuesta esperado
    summary="Clasificar un mensaje usando un modelo zero-shot",  # Resumen para la documentación Swagger
    response_description="Resultado de la clasificación del mensaje",  # Descripción de la respuesta para Swagger
    tags=["Clasificación"]  # Tag personalizado para agrupar el endpoint en Swagger
)
async def clasificar_mensaje(msg: Message, request: Request):
    """
    Clasifica un mensaje usando un modelo zero-shot NLP.

    - **msg**: Objeto con el mensaje a clasificar.
    - **request**: Información de la petición HTTP.

    Devuelve la categoría y score predicho para el mensaje.
    """
    # Registrar la IP del cliente que hace la petición
    logger.info(f"Petición recibida desde {request.client.host}")
    mensaje = msg.mensaje.strip()  # Limpiar espacios en blanco
    if not mensaje:
        # Si el mensaje está vacío, registrar advertencia y lanzar error 400
        logger.warning("Mensaje vacío recibido")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El mensaje no puede estar vacío.")
    try:
        # Clasificar el mensaje usando el modelo
        resultado = classify_message(mensaje)
        return resultado
    except Exception as e:
        # Capturar y registrar errores inesperados
        logger.error(f"Error al clasificar el mensaje: {e}")
        raise HTTPException(status_code=500, detail="Error interno al clasificar el mensaje.")
