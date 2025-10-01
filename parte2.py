import streamlit as st

def parte2():
    st.markdown("# <span style='color:yellow'>📊 Parte II: Limitaciones de la regresión</span>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## <span style='color:red'>1. Inestabilidad de los parámetros:", unsafe_allow_html=True)
        st.markdown("#### Los coeficientes estimados pueden cambiar con el tiempo debido a la naturaleza dinámica de la economía y los mercados financieros. Esto significa que un modelo que funciona en un periodo puede dejar de ser útil si cambian las condiciones del entorno o si más agentes adoptan la misma estrategia.")
    with col2:
        st.markdown("## <span style='color:red'>2. Mezcla de poblaciones:", unsafe_allow_html=True)
        st.markdown("#### Si se combinan datos de diferentes grupos (por ejemplo, países o sectores) sin distinguirlos, el modelo puede no reflejar correctamente la realidad de ninguno de ellos, ya que las relaciones pueden variar entre grupos.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## <span style='color:red'>3. Supuestos teóricos:", unsafe_allow_html=True)
        st.markdown("#### El análisis de regresión depende de supuestos como linealidad, independencia de los errores, homocedasticidad, ausencia de multicolinealidad y normalidad de los residuos. Si estos supuestos se violan, las estimaciones pueden ser poco confiables o sesgadas.")
    with col2:
        st.markdown("## <span style='color:red'>4. Sensibilidad a valores atípicos:", unsafe_allow_html=True)
        st.markdown("#### Los outliers o datos extremos, comunes en finanzas, pueden distorsionar los resultados y hacer que una sola observación tenga un impacto desproporcionado en el modelo.")
    st.markdown("## <span style='color:red'>5. Correlaciones espurias:", unsafe_allow_html=True)
    st.markdown("#### Una relación estadística entre dos variables no implica causalidad. Es posible encontrar asociaciones que son coincidencias y no reflejan una relación causal real, especialmente cuando se manejan grandes bases de datos con muchas variables independientes.")

