import logging  # Importa el módulo estándar de logging de Python

# Configura el logging básico para toda la aplicación
logging.basicConfig(
    level=logging.INFO,  # Establece el nivel mínimo de log en INFO
    format="%(asctime)s [%(levelname)s] %(message)s",  # Define el formato de los mensajes de log
)

# Crea un logger específico para la aplicación 'zero_shot_classifier'
logger = logging.getLogger("zero_shot_classifier")
