import streamlit as st
import streamlit as st
from ui import render_header, render_input_area, render_classification_result, render_error, render_historial
from api_client import clasificar_mensaje

# Configuración de la página
st.set_page_config(page_title="Clasificador de Mensajes", layout="centered", page_icon="📨")

# Renderizar encabezado profesional
render_header()

# Inicializar historial en session_state
if 'historial' not in st.session_state:
    st.session_state['historial'] = []

# Renderizar área de entrada
mensaje = render_input_area()

# Botón para clasificar con fondo personalizado
st.markdown("""
    <style>
    div.stButton > button {
        background: linear-gradient(90deg, #27ae60 0%, #2980b9 100%) !important;
        color: white !important;
        font-weight: 600;
        font-size: 1.1em;
        border-radius: 8px !important;
        border: none;
        padding: 0.75em 0;
        margin-bottom: 10px;
        box-shadow: 0 2px 8px rgba(39,174,96,0.09);
        transition: background 0.3s;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #2980b9 0%, #27ae60 100%) !important;
    }
    </style>
""", unsafe_allow_html=True)
if st.button("🎯 Clasificar", use_container_width=True):
    if not mensaje or not mensaje.strip():
        st.warning("Por favor, ingrese un mensaje.")
    else:
        with st.spinner("Clasificando mensaje..."):
            datos, error = clasificar_mensaje(mensaje)
            if datos:
                render_classification_result(datos)
                # Guardar en historials
                st.session_state['historial'].append({
                    'mensaje': mensaje,
                    'categoria': datos['categoria'],
                    'confianza': datos['confianza']
                })
            else:
                render_error(error)

# Botón para limpiar historial
if st.button("🧹 Limpiar historial", use_container_width=True):
    st.session_state['historial'] = []
    st.success("Historial limpiado.")

# Mostrar historial debajo del área de clasificación
render_historial(st.session_state['historial'])

# --- Exportar historial filtrado como CSV o PDF ---
import pandas as pd
import io
from fpdf import FPDF
import datetime

def exportar_historial():
    historial = st.session_state['historial']
    if not historial:
        st.info("No hay mensajes para exportar.")
        return
    df = pd.DataFrame(historial)
    categorias = ['Todas'] + sorted(df['categoria'].unique())
    filtro = st.selectbox("Filtrar por categoría para exportar:", categorias, key="filtro_exportar")
    if filtro != 'Todas':
        df = df[df['categoria'] == filtro]
    st.markdown("Descarga un informe CSV o PDF de los mensajes clasificados según el filtro seleccionado.")
    # CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Exportar informe CSV",
        data=csv,
        file_name=f'informe_mensajes_{filtro.lower() if filtro != "Todas" else "todas"}.csv',
        mime='text/csv',
        use_container_width=True
    )
    # PDF
    if 'pdf_preview' not in st.session_state:
        st.session_state['pdf_preview'] = None
    if st.button("👁️ Previsualizar PDF", use_container_width=True):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 12, "Informe de Mensajes Clasificados", ln=1, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Fecha de generación: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=1)
        pdf.cell(0, 10, f"Categoría: {filtro}", ln=1)
        pdf.cell(0, 10, f"Total de mensajes: {len(df)}", ln=1)
        pdf.ln(4)
        # Encabezados de tabla
        pdf.set_font("Arial", "B", 12)
        pdf.cell(100, 8, "Mensaje", border=1)
        pdf.cell(35, 8, "Categoría", border=1)
        pdf.cell(25, 8, "Confianza", border=1, ln=1)
        pdf.set_font("Arial", "", 11)
        # Filas de la tabla
        for _, row in df.iterrows():
            mensaje = (row['mensaje'][:60] + '...') if len(row['mensaje']) > 60 else row['mensaje']
            pdf.cell(100, 8, mensaje, border=1)
            pdf.cell(35, 8, str(row['categoria']), border=1)
            pdf.cell(25, 8, f"{row['confianza']:.2f}", border=1, ln=1)
        pdf_output = pdf.output(dest='S')
        if isinstance(pdf_output, bytearray):
            pdf_output = bytes(pdf_output)
        st.session_state['pdf_preview'] = pdf_output
    # Mostrar previsualización si existe
    if st.session_state.get('pdf_preview'):
        import base64
        pdf_base64 = base64.b64encode(st.session_state['pdf_preview']).decode('utf-8')
        st.markdown("""
        <h5>Previsualización del PDF generado:</h5>
        <iframe src="data:application/pdf;base64,{0}" width="100%" height="500px" type="application/pdf"></iframe>
        """.format(pdf_base64), unsafe_allow_html=True)

exportar_historial()
