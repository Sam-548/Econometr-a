import streamlit as st
from parte1 import parte1
from parte2 import parte2
from parte3 import parte3
from parte4 import parte4

#config pagina principal

st.set_page_config(
    page_title="Proyecto Final Econometría",
    page_icon="📊",
    layout="wide"
)

if st.sidebar.button("🔄 Refrescar app"):
    st.rerun()

#barra lateral

st.sidebar.title("PREGUNTAS")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "Parte I: Modelo de Índice Único",
        "Parte II: Limitaciones de la Regresión",
        "Parte III: Ejemplos CFA",
        "Parte IV: Bienes Raíces"])

if seccion == "Parte I: Modelo de Índice Único":
    parte1()

elif seccion == "Parte II: Limitaciones de la Regresión":
    parte2()

elif seccion == "Parte III: Ejemplos CFA":
    parte3()

elif seccion == "Parte IV: Bienes Raíces":
    parte4()