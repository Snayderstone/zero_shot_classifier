from fastapi.testclient import TestClient  # Cliente de pruebas para simular peticiones HTTP
from backend.main import app  # Importa la aplicación FastAPI principal
import pytest

client = TestClient(app)  # Instancia el cliente de pruebas

def test_root_endpoint():
    """
    Prueba el endpoint raíz ('/').
    Espera un status 200 y un mensaje indicando que la API está levantada.
    """
    response = client.get("/")  # Realiza una petición GET a la raíz
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert "Zero-Shot Message Classifier API" in response.json()["message"]  # Verifica el mensaje de bienvenida

def test_clasificar_endpoint_ok():
    """
    Prueba el endpoint '/clasificar/' con un mensaje válido.
    Espera status 200 y que la respuesta contenga las claves esperadas.
    """
    payload = {"mensaje": "Esto es urgente"}  # Mensaje de prueba
    response = client.post("/clasificar/", json=payload)  # Envía el mensaje al endpoint
    assert response.status_code == 200  # Debe responder exitosamente
    data = response.json()
    assert "categoria" in data  # Debe contener la categoría
    assert "confianza" in data  # Debe contener la confianza
    assert data["mensaje"] == payload["mensaje"]  # El mensaje en respuesta debe coincidir

def test_clasificar_endpoint_empty():
    """
    Prueba el endpoint '/clasificar/' con un mensaje vacío.
    Espera status 400 y un mensaje de error específico.
    """
    payload = {"mensaje": "   "}  # Mensaje vacío (solo espacios)
    response = client.post("/clasificar/", json=payload)
    assert response.status_code == 400  # Debe responder con error 400
    assert response.json()["detail"] == "El mensaje no puede estar vacío."

def test_clasificar_endpoint_invalid_schema():
    """
    Prueba el endpoint '/clasificar/' con un esquema inválido (campo incorrecto).
    Espera status 422 indicando entidad no procesable.
    """
    payload = {"msg": "faltante"}  # Falta el campo correcto 'mensaje'
    response = client.post("/clasificar/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
