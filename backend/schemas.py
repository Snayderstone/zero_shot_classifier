from pydantic import BaseModel, Field  # Importa BaseModel y Field para definir esquemas de datos
from typing import Dict  # Importa Dict para tipos de datos de diccionario

class Message(BaseModel):
    """
    Modelo para la petición de entrada.
    Contiene el mensaje que se desea clasificar.
    """
    mensaje: str = Field(..., description="Mensaje a clasificar")  # Campo requerido con descripción para la documentación

class MessageResponse(BaseModel):
    """
    Modelo para la respuesta de la API.
    Incluye el mensaje original, la categoría predicha, el score de confianza y los detalles de todas las categorías.
    """
    mensaje: str  # Mensaje original clasificado
    categoria: str  # Categoría predicha por el modelo
    confianza: float  # Score de confianza de la categoría principal
    detalles: Dict[str, float]  # Diccionario con todas las categorías y sus scores
