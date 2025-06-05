from transformers import pipeline  # Importa el pipeline de transformers para clasificación zero-shot
from .config import LABELS        # Importa las etiquetas candidatas desde el archivo de configuración

# Inicializa el clasificador zero-shot usando el modelo preentrenado de Facebook
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_message(mensaje: str) -> dict:
    """
    Clasifica el mensaje recibido usando el modelo zero-shot.
    Args:
        mensaje (str): El mensaje a clasificar.
    Returns:
        dict: Diccionario con el mensaje, categoría, confianza y detalles.
    """
    resultado = classifier(mensaje, candidate_labels=LABELS)  # Ejecuta la clasificación
    return {
        "mensaje": mensaje,  # Mensaje original
        "categoria": resultado["labels"][0],  # Categoría con mayor score
        "confianza": resultado["scores"][0],  # Score de la categoría principal
        "detalles": dict(zip(resultado["labels"], resultado["scores"]))  # Todas las categorías y scores
    }
