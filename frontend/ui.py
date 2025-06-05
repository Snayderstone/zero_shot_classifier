import streamlit as st
import pandas as pd

def render_header():
    # Colores adaptativos para modo claro/oscuro
    st.markdown("""
        <h1 style='text-align: center; color: var(--text-color, #e1e1e1);'>📨 Clasificador de Mensajes Zero-Shot</h1>
        <p style='text-align: center; color: var(--text-color-secondary, #b0b0b0);'>Ingrese un mensaje para clasificarlo como <b>Urgente</b>, <b>Normal</b> o <b>Moderado</b>.</p>
    """, unsafe_allow_html=True)

def render_input_area():
    st.subheader("Ingrese su mensaje:")
    return st.text_area("Mensaje", height=100, key="mensaje_input")

import plotly.graph_objects as go
import numpy as np

def render_classification_result(datos):
    # Colores por categoría
    categoria = datos['categoria'].lower()
    color_categoria = {
        'normal': '#27ae60',    # verde
        'urgente': '#e74c3c',  # rojo
        'moderado': '#f1c40f'  # amarillo
    }
    color_bg = {
        'normal': 'linear-gradient(90deg, #27ae60 0%, #6dd5ed 100%)',
        'urgente': 'linear-gradient(90deg, #e74c3c 0%, #f85032 100%)',
        'moderado': 'linear-gradient(90deg, #f1c40f 0%, #f9d423 100%)'
    }
    color = color_categoria.get(categoria, '#27ae60')
    bg = color_bg.get(categoria, 'linear-gradient(90deg, #27ae60 0%, #6dd5ed 100%)')

    st.markdown(f"""
        <div style='padding:10px 0 18px 0; margin-bottom:10px; animation: fadein 1.2s;'>
            <span style='font-size:1.35em;'><b>Categoría:</b> <span style='color:{color}'>{datos['categoria']}</span></span><br>
            <b>Confianza:</b> <span style='color:#2980b9'>{datos['confianza']:.2f}</span>
        </div>
        <style>
        @keyframes fadein {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        </style>
    """, unsafe_allow_html=True)
    st.subheader("Detalles de la Clasificación:")
    # Gráfico personalizado con colores por barra
    df = pd.DataFrame.from_dict(datos["detalles"], orient='index', columns=['Confianza'])
    df = df.sort_values(by="Confianza", ascending=False)
    colores = []
    for cat in df.index:
        cat_l = cat.lower()
        if cat_l == 'normal':
            colores.append('rgba(39,174,96,0.85)')
        elif cat_l == 'urgente':
            colores.append('rgba(231,76,60,0.85)')
        elif cat_l == 'moderado':
            colores.append('rgba(241,196,15,0.85)')
        else:
            colores.append('rgba(52,73,94,0.85)')
    # Degradado animado simulando con opacidad
    fig = go.Figure(
        data=[go.Bar(
            x=df.index,
            y=df['Confianza'],
            marker_color=colores,
            text=[f"{v:.2f}" for v in df['Confianza']],
            textposition='auto',
            hoverinfo='x+y',
            marker_line_width=1.5,
            marker_line_color='#222',
        )]
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        bargap=0.3,
        margin=dict(l=20, r=20, t=30, b=30),
        xaxis=dict(title="Categoría", tickfont=dict(size=14)),
        yaxis=dict(title="Confianza", range=[0,1], tickfont=dict(size=14)),
        transition = {"duration": 700, "easing": "cubic-in-out"}
    )
    st.plotly_chart(fig, use_container_width=True)

def render_error(error_msg):
    st.error(error_msg)

def render_historial(historial):
    st.markdown("<h3 style='color:var(--primary-color,#2980b9);margin-top:32px;'>Historial de Clasificaciones</h3>", unsafe_allow_html=True)
    if historial:
        for item in reversed(historial):
            st.markdown(f"""
                <div style='border:1px solid #444;padding:10px 14px;margin-bottom:10px;border-radius:8px;background:rgba(44,62,80,0.25);'>
                    <b>Mensaje:</b> <span style='color:#f1c40f'>{item['mensaje']}</span><br>
                    <b>Categoría:</b> <span style='color:#27ae60'>{item['categoria']}</span><br>
                    <b>Confianza:</b> <span style='color:#2980b9'>{item['confianza']:.2f}</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Aún no hay mensajes clasificados.")
