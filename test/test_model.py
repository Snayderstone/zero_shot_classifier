import sys  # Importa el módulo sys para manipular el path de búsqueda de módulos
import os  # Importa os para operaciones con rutas de archivos
# Agrega el directorio padre al sys.path para permitir importar el backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.model import classify_message  # Importa la función a probar
import pytest  # Importa pytest para las pruebas

def test_classify_message_returns_dict():
    """
    Prueba que classify_message devuelva un diccionario con las claves esperadas
    cuando se le pasa un mensaje válido.
    """
    mensaje = "Necesito ayuda urgente"
    resultado = classify_message(mensaje)
    # Verifica que el resultado sea un diccionario
    assert isinstance(resultado, dict)
    # Verifica que tenga las claves esperadas
    assert "mensaje" in resultado
    assert "categoria" in resultado

def test_classify_message_empty_string():
    """
    Prueba que classify_message lance una excepción si el mensaje es vacío.
    """
    mensaje = ""
    with pytest.raises(Exception):
        classify_message(mensaje)

def test_classify_message_not_string():
    """
    Prueba que classify_message lance una excepción si el mensaje no es un string.
    """
    mensaje = None
    with pytest.raises(Exception):
        classify_message(mensaje)
