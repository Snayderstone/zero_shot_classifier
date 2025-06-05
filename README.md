# 📨 Clasificador de Mensajes Zero-Shot

Proyecto completo de clasificación de mensajes usando un modelo Zero-Shot NLP, con backend en **FastAPI** y frontend profesional en **Streamlit**.

## 🚀 Descripción
Esta aplicación permite clasificar mensajes de texto en tres categorías: **Urgente**, **Normal** y **Moderado**, usando técnicas de NLP Zero-Shot. Incluye:
- Backend robusto con FastAPI y endpoints documentados.
- Frontend moderno y responsivo con Streamlit, con historial de clasificaciones, visualizaciones y exportación de informes.

---

## 📁 Estructura del Proyecto
```
zero_shot_classifier/
├── backend/                  # Backend FastAPI
│   ├── api.py
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
├── frontend/                 # Frontend Streamlit
│   ├── api_client.py
│   ├── app.py
│   ├── ui.py
├── test/                     # Tests (backend y posibles utilidades)
│   ├── test_api.py
│   ├── test_logger.py
│   ├── test_model.py
│   ├── test_schemas.py
├── .python-version           # Versión de Python del proyecto
├── pyproject.toml            # Dependencias y configuración de uv
├── uv.lock                   # Archivo de lock de uv
├── README.md                 # Este archivo


```

---

## ⚙️ Instalación y Configuración
1. **Clona el repositorio:**
   ```bash
   git clone <REPO_URL>
   cd zero_shot_classifier
   ```
2. **Crea y activa un entorno virtual (opcional):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate    # Windows
   ```
3. **Instala dependencias con [uv](https://github.com/astral-sh/uv):**
   ```bash
   uv pip install -r pyproject.toml
   ```
   O simplemente:
   ```bash
   uv sync
   ```
   *(uv detecta y usa pyproject.toml para gestionar dependencias, no uses requirements.txt)*
4. **Configura el archivo `.env`:**
   Crea un archivo `.env` en la raíz del proyecto con:
   ```env
   API_URL=http://localhost:8000/clasificar/
   ```
   Cambia la URL según tu entorno de backend.

---

## 🖥️ Ejecución
### 1. Backend (FastAPI)
En la raíz del proyecto:
```bash
uvicorn backend.main:app --reload
```
El backend estará disponible en `http://localhost:8000`.

### 2. Frontend (Streamlit)
```bash
uv run streamlit run frontend/app.py
```
*(O simplemente usa `streamlit run frontend/app.py` si ya tienes el entorno activado con uv)*

---

## 📝 Uso de la Aplicación
1. Ingresa un mensaje en la caja de texto.
2. Haz clic en **"Clasificar"** para ver la categoría y confianza.
3. El historial de clasificaciones se muestra abajo.
4. Puedes limpiar el historial con el botón correspondiente.
5. Exporta un informe de tus mensajes clasificados:
   - **CSV**: descarga filtrando por categoría.
   - **PDF**: previsualiza y descarga un informe profesional.

---

## 📦 Funcionalidades Destacadas
- Clasificación Zero-Shot NLP (sin entrenamiento específico).
- Visualización con colores y gráficos modernos (Plotly).
- Historial persistente en sesión.
- Exportación de informes filtrados (CSV y PDF, con previsualización).
- Código limpio, modular y fácil de mantener.

---

## 👤 Créditos
- Proyecto para fines educativos y profesionales.

¿Dudas, sugerencias o mejoras? ¡Contáctame o abre un issue!
