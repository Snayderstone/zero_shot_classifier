from fastapi import FastAPI  # Importa la clase principal de FastAPI
from .api import router    # Importa las rutas definidas en api.py

# Crea la aplicación FastAPI con un título personalizado
app = FastAPI(title="Zero-Shot Message Classifier")
# Incluye el router con los endpoints definidos en api.py
app.include_router(router)
