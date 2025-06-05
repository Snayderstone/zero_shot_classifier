from backend.schemas import Message, MessageResponse  # Importa los modelos de datos a probar
import pytest  # Importa pytest para las pruebas
from pydantic import ValidationError  # Importa el error de validación de Pydantic

def test_message_schema_valid():
    """
    Prueba que el esquema Message acepte un mensaje válido.
    """
    msg = Message(mensaje="Hola mundo")
    assert msg.mensaje == "Hola mundo"

def test_message_schema_empty():
    """
    Prueba que el esquema Message rechace un mensaje vacío o None.
    """
    with pytest.raises(ValidationError):
        Message(mensaje=None)

def test_message_response_schema_valid():
    """
    Prueba que el esquema MessageResponse acepte datos válidos.
    """
    resp = MessageResponse(
        mensaje="Hola mundo",
        categoria="Normal",
        confianza=0.9,
        detalles={"Normal": 0.9, "Urgente": 0.1}
    )
    assert resp.categoria == "Normal"

def test_message_response_schema_invalid_confianza():
    """
    Prueba que el esquema MessageResponse rechace un valor no numérico en 'confianza'.
    """
    with pytest.raises(ValidationError):
        MessageResponse(
            mensaje="Hola mundo",
            categoria="Normal",
            confianza="no_es_float",
            detalles={"Normal": 0.9}
        )
