import logging  # Importa el módulo de logging estándar de Python
import pytest  # Importa pytest para las pruebas
from backend.logger import logger  # Importa el logger configurado en el backend

def test_logger_info_message(caplog):
    """
    Prueba que el logger registre correctamente un mensaje de nivel INFO.
    Utiliza caplog para capturar los logs generados durante la prueba.
    """
    # Establece el nivel de captura en INFO
    with caplog.at_level(logging.INFO):
        logger.info("Mensaje de prueba INFO")  # Genera un mensaje de log de nivel INFO
        # Verifica que el mensaje esté presente en los logs capturados
        assert any("Mensaje de prueba INFO" in m for m in caplog.messages)

def test_logger_warning_message(caplog):
    """
    Prueba que el logger registre correctamente un mensaje de nivel WARNING.
    Utiliza caplog para capturar los logs generados durante la prueba.
    """
    # Establece el nivel de captura en WARNING
    with caplog.at_level(logging.WARNING):
        logger.warning("Mensaje de prueba WARNING")  # Genera un mensaje de log de nivel WARNING
        # Verifica que el mensaje esté presente en los logs capturados
        assert any("Mensaje de prueba WARNING" in m for m in caplog.messages)
