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
   git clone https://github.com/Snayderstone/zero_shot_classifier.git
   cd zero_shot_classifier
   ```
2. **Instala el gestor de paquetes uv:**
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" # para windows
   curl -LsSf https://astral.sh/uv/install.sh | sh # para linux o mac
   pip install uv #usando pip
   uv --version # para verificar la instalación
   ```
3. **Crea y activa un entorno virtual (opcional):**
   ```bash
   uv venv .venv #crea un entorno virtual con uv
   source .venv/bin/activate #activa el entorno virtual
   ```
4. **Instala dependencias con [uv](https://github.com/astral-sh/uv):**
   ```bash
   uv pip install -r pyproject.toml
   ```
   O simplemente:
   ```bash
   uv sync
   ```
   *(uv detecta y usa pyproject.toml para gestionar dependencias, no uses requirements.txt)*
5. **Configura el archivo `.env`:**
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
uvicorn backend.main:app
```
El backend estará disponible en `http://localhost:8000`.

### 2. Frontend (Streamlit)
```bash
streamlit run frontend/app.py
```
El frontend estará disponible en `http://localhost:8501`

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

## 🖼️ Capturas de Pantalla

### Backend (FastAPI)

![Documentación interactiva de la API](images/backend1.png)
*Documentación automática generada por FastAPI.*

![Respuesta de ejemplo de la API](images/backend2.png)
*Ejemplo de respuesta JSON del endpoint de clasificación.*

### Frontend (Streamlit)

#### Pantalla principal para ingresar y clasificar mensajes.

![Interfaz principal de la app](images/frontend1.png)

#### Visualización de la categoría y confianza, con colores y gráficos.

![Resultado de clasificación](images/frontend2.png)

#### Historial persistente en la sesión, con opción de limpiar.

![Historial de clasificaciones](images/frontend3.png)

#### Opciones para exportar el historial filtrado como PDF o CSV, con previsualización.

![Exportar informe PDF y CSV](images/frontend4.png)


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
