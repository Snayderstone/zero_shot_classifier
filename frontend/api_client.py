import os
from dotenv import load_dotenv
import requests

# Cargar variables del archivo .env (incluyendo API_URL)
load_dotenv()

# URL del endpoint backend, OBLIGATORIA por variable de entorno o .env
API_URL = os.environ.get("API_URL")
if not API_URL:
    raise RuntimeError("La variable de entorno API_URL es obligatoria. Defínela en tu .env o entorno de ejecución.")


def clasificar_mensaje(mensaje: str, api_url: str = API_URL):
    """
    Envía el mensaje a la API y devuelve la respuesta o el error.
    Por defecto usa la URL definida en la variable de entorno API_URL.
    """
    try:
        respuesta = requests.post(api_url, json={"mensaje": mensaje})
        if respuesta.status_code == 200:
            return respuesta.json(), None
        else:
            return None, respuesta.json().get("detail", respuesta.text)
    except Exception as e:
        return None, str(e)