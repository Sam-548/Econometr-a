import streamlit as st
import subprocess

def parte1():
    # 1.1
    st.markdown("# <span style='color:yellow'>📊 Parte I: Modelo de Índice Único</span>", unsafe_allow_html=True)
    st.markdown("## <span style='color:yellow'>**Contexto del análisis**</span>", unsafe_allow_html=True)
    st.markdown("##### Este informe presenta el análisis completo del Modelo de Índice Único aplicado a tres compañías líderes del sector tecnológico: NVIDIA Corporation (NVDA), Texas Instruments Incorporated (TXN), e Intel Corporation (INTC). El estudio utiliza datos históricos desde junio 2023 hasta agosto 2025.")
    st.markdown("##### Para la elaboración de este ejercicio se utilizó el Modelo de Índice Único")
    st.markdown("### <span style='color:#FF8C00'>Ri,t=αi+βiRm,t+ϵi,t</span>", unsafe_allow_html=True)
    st.markdown("##### • Ri,t: Retorno del activo i en el tiempo t")
    st.markdown("##### • Rm,t: Retorno del mercado (NASDAQ) en el tiempo ")
    st.markdown("##### • βi: Coeficiente de riesgo sistemático")
    st.markdown("##### • αi: Intercepto (retorno específico)")
    st.markdown("##### • ϵi,t: Término de error (riesgo específico)t</span>")

    st.markdown("# <span style='color:yellow'>📀 Punto 1.1</span>", unsafe_allow_html=True)
    st.markdown("##### Al estimar la ecuación de regresión obtuvimos:")
    st.markdown("### <span style='color:#FF8C00'>R_NVDA,t = α + β × R_NASDAQ,t + εt</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>R_NVDA,t = 0.1415 + 1.8351 × R_NASDAQ,t</span>", unsafe_allow_html=True)
    st.code(""" # MODELO PARA NVIDIA (NVDA) - CÁLCULO DE LA ECUACIÓN
modelo_nvda <- analizar_regresion_completo(datos_retornos$R_NVDA, datos_retornos$R_NASDAQ, "NVIDIA (NVDA)")
cat("Ecuación estimada:")
cat("R_NVDA,t = α + β × R_NASDAQ,t + εt")
cat("R_NVDA,t = ", round(modelo_nvda$alpha, 4), " + ", round(modelo_nvda$beta, 4), 
" × R_NASDAQ,t", sep = "" """)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### El coeficiente β mide la sensibilidad de NVIDIA a los movimientos del mercado, e indica el riego sistemático de la acción.")
        st.markdown("##### Por cada 1% de movimiento del NASDAQ, NVIDIA se mueve aproximadamente 1,8351% en la misma dirección.")
        st.markdown("##### <span style='color:#FF8C00'>En este caso, *β = 1.8351* y según la clasificación del riesgo, si β > 1, se considera una acción agresiva,  es decir, de alto riesgo y retorno y, por ende, más volátil que el mercado.</span>", unsafe_allow_html=True)
    with col1:
        st.code(""" # INTERPRETACIÓN DEL BETA
cat("Interpretación del coeficiente β:")
cat("• β = ", round(modelo_nvda$beta, 4), sep = "")
cat("• Por cada 1% de movimiento del NASDAQ, NVIDIA se mueve aproximadamente ", 
round(modelo_nvda$beta, 4), "% en la misma dirección", sep = "" """)
        st.code(""" # CLASIFICACIÓN DEL RIESGO SEGÚN BETA
cat("Clasificación del riesgo según β:")
if(modelo_nvda$beta > 1) {
cat("• β > 1: Acción AGRESIVA - Alto riesgo y alto retorno esperado")
cat("• Más volátil que el mercado")
cat("• Considerada de alto riesgo sistemático")
} else if(modelo_nvda$beta < 1) {
cat("• β < 1: Acción DEFENSIVA - Menor riesgo que el mercado") 
cat("• Menos volátil que el mercado")
} else {
cat("• β = 1: Mismo riesgo que el mercado")
} """)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### Al calcular Ke para NVDA obtuvimos:")
        st.markdown("##### <span style='color:#FF8C00'>Fórmula: Ke = Rf + β × (Rm - Rf)</span>", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>Ke = 2.5 + 1.8351 × (10 - 2.5) = 16.26% anual</span>", unsafe_allow_html=True)
        st.markdown("##### Para esto, utilizamos los supuestos de que la tasa libre libre de riesgo = 2,5% y que el retorno esperado del mercado = 10%.")
        st.markdown("##### <span style='color:#FF8C00'>Lo cual significa que NVIDIA debe generar retornos iguales o superiores al 16,26% anual para compensar el riesgo asumido por los inversionistas. En otras palabras, es la tasa mínima de retorno que deben esperar los accionistas.</span>", unsafe_allow_html=True)
    with col1:
        st.code(""" # CÁLCULO DEL Ke PARA NVIDIA (MODELO CAPM)
Rf <- 2.5   # Tasa libre de riesgo (supuesto razonable)
Rm <- 10    # Retorno esperado del mercado (supuesto razonable)
Ke_nvda <- Rf + modelo_nvda$beta * (Rm - Rf)
cat("Ke = ", Rf, " + ", round(modelo_nvda$beta, 4), " × (", Rm, " - ", Rf, ") = ", 
round(Ke_nvda, 2), "% anual", sep = "") """)
        st.code(""" # INTERPRETACIÓN DEL Ke
cat("Interpretación del Ke calculado:")
cat("• NVIDIA debe generar retornos iguales o superiores al ", round(Ke_nvda, 2), 
    "% anual para compensar el riesgo asumido", sep = "")
cat("• Es la tasa mínima de retorno que deben esperar los accionistas")
cat("• Representa el costo de oportunidad del capital para inversiones de similar riesgo")

cat("Supuestos utilizados:")
cat("• Tasa libre de riesgo (Rf) = ", Rf, sep = "")
cat("• Retorno esperado del mercado (Rm) = ", Rm, sep = "")
cat("• Beta de NVIDIA (β) = ", round(modelo_nvda$beta, 4), sep = "") """)

    # 1.2 
    st.markdown("# <span style='color:yellow'>📈 Punto 1.2</span>", unsafe_allow_html=True)
    st.markdown("##### Para determinar si la acción de la empresa NVIDIA tiene el mismo nivel de riesgo que el mercado entero realizamos las siguientes hipótesis:")
    st.markdown("### <span style='color:#FF8C00'>• H0: β = 1 -> NVIDIA tiene el MISMO riesgo que el mercado</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>• H1: β ≠ 1 -> NVIDIA tiene un riesgo DIFERENTE al mercado</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>• Nivel de significancia: α = 0.05</span>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### Y los resultados fueron:")
        st.markdown("##### <span style='color:#FF8C00'>• Beta estimada: 1,8351</span> -> Mucho más volátil que el mercado H0", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>• Error estadístico: 0,0651</span>", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>• Estadistico t: 12,8219</span> -> Indica que la diferencia entre el beta observado (1.8351) y el beta hipotético (1.0) es 12.82 veces mayor que la variabilidad esperada por error de muestreo.", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>• P-valor: 0,0000</span> -> Significa que la probabilidad de observar un beta de 1.8351 si NVIDIA realmente tuviera el mismo riesgo que el mercado es nula.", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>Existe evidencia extremadamente fuerte para afirmar que NVIDIA tiene un nivel de riesgo significativamente diferente al del mercado.</span>", unsafe_allow_html=True)
    with col1:
        st.code(""" # Parámetros y cálculos
beta_est     <- modelo_nvda$beta
error_est    <- modelo_nvda$resumen$coefficients[2, 2]
t_stat       <- (beta_est - 1) / error_est
p_val        <- modelo_nvda$p_valor_beta1
alpha        <- 0.05 """)
        st.code(""" # Hipótesis
cat("=== HIPÓTESIS ===")
cat("H0: β = 1  -> NVIDIA tiene el MISMO riesgo que el mercado")
cat("H1: β ≠ 1  -> NVIDIA tiene un riesgo DIFERENTE al mercado")
cat("Nivel de significancia: α =", alpha)""")
        st.code(""" # Decisión
cat("=== DECISIÓN ===")
if (p_val < alpha) {
  cat("RECHAZAR H0")
  cat("Conclusión: NVIDIA tiene un nivel de riesgo DIFERENTE al del mercado.")
  cat("Justificación: p-valor < α indica evidencia significativa contra H0.")
} else {
  cat("NO RECHAZAR H0")
  cat("Conclusión: No hay evidencia suficiente para decir que el riesgo de NVIDIA sea diferente.")
}""")
    
    # 1.3

    st.markdown("# <span style='color:yellow'>📉 Punto 1.3</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>R² = 0.5881 (58.81%)</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>1 - R² = 0.4119 (41.19%)</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### Interpretación:")
        st.markdown("##### • 58.8% del riesgo total de NVIDIA corresponde al riesgo de mercado.")
        st.markdown("##### • 41.2% puede atribuirse al riesgo específico de la compañía.")
        st.markdown("##### • El riesgo de mercado es no diversificable, el riesgo específico sí se puede diversificar.")
    with col1:
        st.code(""" # COMPOSICIÓN DEL RIESGO
riesgo_mercado <- modelo_nvda$r_cuadrado * 100
riesgo_especifico <- (1 - modelo_nvda$r_cuadrado) * 100

cat("R² = ", round(modelo_nvda$r_cuadrado, 4), " (", round(riesgo_mercado, 2), sep = "")
cat("1 - R² = ", round(1 - modelo_nvda$r_cuadrado, 4), " (", round(riesgo_especifico, 2), sep = "")

cat("Interpretación:\n")
cat("• ", round(riesgo_mercado, 1), "% del riesgo total de NVIDIA corresponde al riesgo de mercado", sep = "")
cat("• ", round(riesgo_especifico, 1), "% puede atribuirse al riesgo específico de la compañía", sep = "")
cat("• El riesgo de mercado es no diversificable, el riesgo específico sí se puede diversificar")""")
    
    # 1.4
    st.markdown("# <span style='color:yellow'>💵 Punto 1.4</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### Interpretación: Al calcular la correlación que existe entre el retorno diario del índice NASDAQ y el retorno diario de la acción NVDA obtuvimos:")
        st.markdown("##### <span style='color:#FF8C00'>Coeficiente de correlación: 0.7669</span>", unsafe_allow_html=True)
        st.markdown("##### Es un coeficiente positivo, el cual indica que NVIDIA tiende a moverse en la misma dirección que el NASDAQ.")
        st.markdown("##### El 76.69% de la variación en los retornos de NVIDIA puede explicarse por su relación   lineal con los movimientos del NASDAQ.")
        st.markdown("##### <span style='color:#FF8C00'>• Cuando el NASDAQ SUBE → NVIDIA tiende a SUBIR", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>• Cuando el NASDAQ BAJA → NVIDIA tiende a BAJAR", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>• La dirección es CONSISTENTE en 76.69% de los casos", unsafe_allow_html=True)
    with col1:
        st.code(""" # CORRELACIÓN ENTRE NVIDIA Y NASDAQ
cat("• Coeficiente de correlación: ", round(modelo_nvda$correlacion, 4), sep = "")
                                
if(modelo_nvda$correlacion > 0.7) {
  cat("• Interpretación: Correlación FUERTE y positiva")
} else if(modelo_nvda$correlacion > 0.3) {
  cat("• Interpretación: Correlación MODERADA y positiva") 
} else {
  cat("• Interpretación: Correlación DÉBIL y positiva")
}""")
        st.image("/Users/sam/Desktop/eco.py/Rplot.png", use_container_width=True)

    # 1.5 
    st.markdown("# <span style='color:yellow'>💵 Punto 1.5</span>", unsafe_allow_html=True)
    st.markdown("## Solo mide las relaciones lineales")
    st.markdown("## Sensibilidad a valores atípicos")
    st.markdown("## Posibles interpretaciones engañosas)")

    # 1.6 A)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (A)</span>", unsafe_allow_html=True)
    st.markdown("##### Misma prueba de hipótesis (β = 1) para ambas empresas:")
    st.code("""# Estimar modelos para TXN e INTC
modelo_txn <- analizar_regresion_completo(datos_retornos$R_TXN, datos_retornos$R_NASDAQ, "Texas Instruments (TXN)")
modelo_intc <- analizar_regresion_completo(datos_retornos$R_INTC, datos_retornos$R_NASDAQ, "Intel (INTC)")""")
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("### <span style='color:#FF8C00'>¿Texas Instruments (TXN) tiene el mismo nivel de riesgo que el mercado?</span>", unsafe_allow_html=True)
        st.markdown("##### • β = 0.9929")
        st.markdown("##### • p-valor (β = 1) = 0.892")
        st.markdown("##### • Conclusión: Riesgo SIMILAR al mercado")
        st.markdown("##### • Justificación: No hay evidencia significativa de diferencia")
        st.markdown("##### <span style='color:#FF8C00'>• Cualquier incremento en el mercado genera el mismo incremento en Texas Instruments (TXN)</span>", unsafe_allow_html=True)
    with col1:
        st.code(""" # ¿TXN E INTC TIENEN EL MISMO RIESGO QUE EL MERCADO?
empresas_6a <- list(
  list(nombre = "Texas Instruments (TXN)", modelo = modelo_txn),
  list(nombre = "Intel (INTC)", modelo = modelo_intc)
)

for(empresa in empresas_6a) {
  cat(empresa$nombre, ":")
  cat("• β = ", round(empresa$modelo$beta, 4), sep = "")
  cat("• p-valor (β = 1) = ", round(empresa$modelo$p_valor_beta1, 4), sep = "")
  
if(empresa$modelo$p_valor_beta1 < 0.05) {
    cat("• Conclusión: Riesgo DIFERENTE al mercado")
    cat("• Justificación: p-valor < 0.05 indica diferencia significativa")
} else {
    cat("• Conclusión: Riesgo SIMILAR al mercado") 
    cat("• Justificación: No hay evidencia significativa de diferencia")
}
cat("• Cualquier incremento en el mercado ", 
      ifelse(empresa$modelo$p_valor_beta1 < 0.05, "NO genera", "genera"),
      " el mismo incremento en ", empresa$nombre, sep = "")
}""")
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("### <span style='color:#FF8C00'>¿Intel (INTC) tiene el mismo nivel de riesgo que el mercado?</span>", unsafe_allow_html=True)
        st.markdown("##### • β = 1.2433")
        st.markdown("##### • p-valor (β = 1) = 0.0098")
        st.markdown("##### • Conclusión: Riesgo DIFERENTE al mercado")
        st.markdown("##### • Justificación: p-valor < 0.05 indica diferencia significativa")
        st.markdown("##### <span style='color:#FF8C00'>• Cualquier incremento en el mercado NO genera el mismo incremento en Intel (INTC)</span>", unsafe_allow_html=True)
    with col1:
        st.image("/Users/sam/Desktop/eco.py/intel.png", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col2:
        st.markdown("### <span style='color:#FF8C00'>Texas Instruments (TXN)</span>", unsafe_allow_html=True)
        st.markdown("##### • El p-valor de 0.892 significa que hay un 89.2% de probabilidad de observar un beta de 0.9929 (o más extremo) si  el verdadero beta fuera 1.0. Esto es muy alto, indicando que la diferencia es INSIGNIFICANTE desde el punto de vista estadístico.")
        st.markdown("##### • Por cada 1% que mueve el NASDAQ, TXN se mueve aproximadamente 1%")
    with col1:
        st.markdown("### <span style='color:#FF8C00'>Intel (INTC)</span>", unsafe_allow_html=True)
        st.markdown("##### • El p-valor de 0.0098 significa que solo hay un 0.98% de probabilidad de observar un beta de 1.2433 (o más extremo) si el verdadero beta fuera 1.0. Esto es muy bajo, proporcionando evidencia contundente de que Intel es más volátil que el mercado.")
        st.markdown("##### • Por cada 1% que mueve el NASDAQ, Intel se mueve aproximadamente 1.24%")
    
    # 1.6 B)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (B)</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### Ranking de sensibilidad al mercado (de mayor a menor):")
        st.markdown("##### 1. NVIDIA (NVDA): β = 1.8351")
        st.markdown("##### 2. Intel (INTC): β = 1.2433")
        st.markdown("##### 3. Texas Instruments (TXN): β = 0.9929")
        st.markdown("##### <span style='color:#FF8C00'>CONCLUSIÓN: NVIDIA (NVDA) es la más sensible, y por ende, la más riesgosa.</span>", unsafe_allow_html=True)
        st.markdown("##### <span style='color:#FF8C00'>CONCLUSIÓN: Texas Instruments (TXN) es la menos sensible, y por ende, la menos riesgosa.</span>", unsafe_allow_html=True)
    with col1:
        st.code(""" # COMPARACIÓN DE SENSIBILIDADES AL MERCADO (NVDA, TXN, INTC)
resultados_betas <- data.frame(
  Empresa = c("NVIDIA (NVDA)", "Texas Instruments (TXN)", "Intel (INTC)"),
  Beta = c(modelo_nvda$beta, modelo_txn$beta, modelo_intc$beta),
  R2 = c(modelo_nvda$r_cuadrado, modelo_txn$r_cuadrado, modelo_intc$r_cuadrado)
)

# Ordenar por beta descendente
resultados_ordenados <- resultados_betas[order(-resultados_betas$Beta), ]

cat("Ranking de sensibilidad al mercado (de mayor a menor):")
for(i in 1:nrow(resultados_ordenados)) {
  cat(i, ". ", resultados_ordenados$Empresa[i], ": β = ", 
      round(resultados_ordenados$Beta[i], 4), sep = "")
}""")

    # 1.6 C)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (C)</span>", unsafe_allow_html=True)
    st.code(""" # COMPOSICIÓN DEL RIESGO PARA TXN E INTC
empresas_6c <- list(
  list(nombre = "Texas Instruments (TXN)", modelo = modelo_txn),
  list(nombre = "Intel (INTC)", modelo = modelo_intc)
)

for(empresa in empresas_6c) {
  riesgo_mercado <- empresa$modelo$r_cuadrado * 100
  riesgo_especifico <- (1 - empresa$modelo$r_cuadrado) * 100
  
  cat("\n", empresa$nombre, sep = "")
  cat("• R² = ", round(empresa$modelo$r_cuadrado, 4), sep = "")
  cat("• Riesgo de mercado: ", round(riesgo_mercado, 2), sep = "")
  cat("• Riesgo específico: ", round(riesgo_especifico, 2), sep = "")
  cat("• Interpretación: ", round(riesgo_mercado, 1), "% del riesgo total corresponde al mercado,", sep = "")
  cat("  ", round(riesgo_especifico, 1), "% es riesgo específico de la compañía", sep = "")
}""")
    st.markdown("### <span style='color:#FF8C00'>¿Qué porcentaje del riesgo total que se tiene al invertir en acciones de TXN corresponde al riesgo de mercado?</span>", unsafe_allow_html=True)
    st.markdown("### • R² = 0.3956")
    st.markdown("### • Riesgo de mercado: 39.56%")
    st.markdown("### <span style='color:#FF8C00'>¿Cuál es el porcentaje que puede atribuirse al riesgo específico de la compañía?</span>", unsafe_allow_html=True)
    st.markdown("### • Riesgo específico: 60.44%")
    st.markdown("### <span style='color:#FF8C00'>¿Qué porcentaje del riesgo total que se tiene al invertir en acciones de INTC corresponde al riesgo de mercado?</span>", unsafe_allow_html=True)
    st.markdown("### • R² = 0.2396")
    st.markdown("### • Riesgo de mercado: 23.96%")
    st.markdown("### <span style='color:#FF8C00'>¿Cuál es el porcentaje que puede atribuirse al riesgo específico de la compañía?</span>", unsafe_allow_html=True)
    st.markdown("### • Riesgo específico: 76.04%")

    # 1.6 D)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (D)</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("### <span style='color:#FF8C00'>CÁLCULO DE Ke PARA TXN E INTC (CAPM)</span>", unsafe_allow_html=True)
        st.markdown("##### Texas Instruments (TXN):")
        st.markdown("##### Ke = 2.5 + 0.9929 × (10 - 2.5) = <span style='color:#FF8C00'>9.95% anual</span>", unsafe_allow_html=True)
        st.markdown("##### Intel (INTC):")
        st.markdown("##### Ke = 2.5 + 1.2433 × (10 - 2.5) = <span style='color:#FF8C00'>11.82% anual", unsafe_allow_html=True)
    with col1:
        st.code("""
for(empresa in empresas_6c) {
  Ke_empresa <- Rf + empresa$modelo$beta * (Rm - Rf)
  cat(empresa$nombre, sep = "")
  cat("Ke = ", Rf, " + ", round(empresa$modelo$beta, 4), 
  " × (", Rm, " - ", Rf, ") = ", 
  round(Ke_empresa, 2), "% anual", sep = "")
}""")

    # 1.6 E)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (E)</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>Datos:</span>", unsafe_allow_html=True)
    st.markdown("### • La firma tiene el mismo nivel de riesgo no diversificable que las acciones de la compañía TXN: ")
    st.markdown("### • El rendimiento promedio diario del portafolio de mercado ha sido de 1.12%.")
    st.markdown("### • Calcular con intervalo de confianza del 95%.")
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### <span style='color:#FF8C00'>Resultados para Texas Instruments (TXN):", unsafe_allow_html=True)
        st.markdown("##### • Retorno esperado: 1.064%")
        st.markdown("##### • Límite inferior IC 95%: 0.8941%")
        st.markdown("##### • Límite superior IC 95%: 1.2339%")
        st.markdown("##### • Intervalo de confianza 95%: [0.8941%, 1.2339%]")
        st.markdown("##### <span style='color:#FF8C00'>Interpretación para la firma de tecnología:", unsafe_allow_html=True)
        st.markdown("##### • Con 95% de confianza, el retorno promedio diario esperado está entre 0.894% y 1.234%.")
        st.markdown("##### • Este intervalo aplica para cualquier firma con el mismo riesgo no diversificable que TXN.")
    with col1:
        st.code("""
                ic_txn <- predict(modelo_txn$modelo, 
                  newdata = data.frame(retorno_mercado = 1.12),
                  interval = "confidence", level = 0.95)

cat("Resultados para Texas Instruments (TXN):")
cat("• Retorno esperado: ", round(ic_txn[1], 4), sep = "")
cat("• Límite inferior IC 95%: ", round(ic_txn[2], 4), sep = "")
cat("• Límite superior IC 95%: ", round(ic_txn[3], 4), sep = "")
cat("• Intervalo de confianza 95%: [", round(ic_txn[2], 4), "%, ", 
    round(ic_txn[3], 4), sep = "")

cat("Interpretación para la firma de tecnología:")
cat("• Con 95% de confianza, el retorno promedio diario esperado está entre ", 
    round(ic_txn[2], 3), "% y ", round(ic_txn[3], 3), sep = "")
cat("• Este intervalo aplica para cualquier firma con el mismo riesgo no diversificable que TXN\n")

cat("6f) INTERVALO DE CONFIANZA 95% PARA LA PENDIENTE (β) DE TXN")

ic_beta_txn <- confint(modelo_txn$modelo, level = 0.95)[2, ]

cat("Intervalo de confianza 95% para β de TXN:")
cat("• β estimado: ", round(modelo_txn$beta, 4), sep = "")
cat("• Límite inferior: ", round(ic_beta_txn[1], 4), sep = "")
cat("• Límite superior: ", round(ic_beta_txn[2], 4), sep = "")
cat("• Intervalo: [", round(ic_beta_txn[1], 4), ", ", round(ic_beta_txn[2], 4), sep = "")

cat("Interpretación: Con 95% de confianza, el verdadero β de TXN está entre ", 
    round(ic_beta_txn[1], 3), " y ", round(ic_beta_txn[2], 3), sep = "")""")

    # 1.6 F)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (F)</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.code(""""
ic_beta_txn <- confint(modelo_txn$modelo, level = 0.95)[2, ]

cat("Intervalo de confianza 95% para β de TXN:\n")
cat("• β estimado: ", round(modelo_txn$beta, 4), "\n", sep = "")
cat("• Límite inferior: ", round(ic_beta_txn[1], 4), "\n", sep = "")
cat("• Límite superior: ", round(ic_beta_txn[2], 4), "\n", sep = "")
cat("• Intervalo: [", round(ic_beta_txn[1], 4), ", ", round(ic_beta_txn[2], 4), "]\n\n", sep = "")

cat("Interpretación: Con 95% de confianza, el verdadero β de TXN está entre ", 
    round(ic_beta_txn[1], 3), " y ", round(ic_beta_txn[2], 3), "\n", sep = "")""")
    
    with col2:
        st.markdown("##### Intervalo de confianza 95% para β de TXN:")
        st.markdown("##### • β estimado: 0.9929")
        st.markdown("##### • Límite inferior: 0.8907")
        st.markdown("##### • Límite superior: 1.0952")
        st.markdown("##### • Intervalo: [0.8907, 1.0952]")
        st.markdown("##### <span style='color:#FF8C00'>Interpretación: Con 95% de confianza, el verdadero β de TXN está entre 0.891 y 1.095", unsafe_allow_html=True)

    # 1.6 G)
    st.markdown("# <span style='color:yellow'>💿 Punto 1.6 (G)</span>", unsafe_allow_html=True)
    st.code("""
cat("Hipótesis:")
cat("• H0: β = 0 (El retorno del NASDAQ no tiene efecto lineal sobre TXN)")
cat("• H1: β ≠ 0 (El retorno del NASDAQ sí tiene efecto lineal sobre TXN)")
cat("• Nivel de significancia: α = 0.05")

cat("Resultados:\n")
cat("• p-valor = ", round(modelo_txn$p_valor_beta0, 6), sep = "")

if(modelo_txn$p_valor_beta0 < 0.05) {
  cat("• Decisión: RECHAZAR H0")
  cat("• Conclusión: Existe evidencia significativa de que el NASDAQ tiene efecto lineal sobre TXN")
} else {
  cat("• Decisión: NO RECHAZAR H0")
  cat("• Conclusión: No hay evidencia suficiente de efecto lineal significativo")
}""")
    st.markdown("### <span style='color:#FF8C00'>PRUEBA DE SIGNIFICANCIA PARA EFECTO LINEAL (TXN)", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>Hipótesis:", unsafe_allow_html=True)
    st.markdown("### • H0: β = 0 (El retorno del NASDAQ no tiene efecto lineal sobre TXN).")
    st.markdown("### • H1: β ≠ 0 (El retorno del NASDAQ sí tiene efecto lineal sobre TXN).")
    st.markdown("### • Nivel de significancia: α = 0.05")
    st.markdown("### <span style='color:#FF8C00'>Resultados:", unsafe_allow_html=True)
    st.markdown("### • p-valor = 0.")
    st.markdown("### • Decisión: RECHAZAR H0.")
    st.markdown("### • Conclusión: Existe evidencia significativa de que el NASDAQ tiene efecto lineal sobre TXN.")
    
    # 1.7 A)
    st.markdown("# <span style='color:yellow'>📡 Punto 1.7 (A)</span>", unsafe_allow_html=True)
    st.markdown("### CONSTRUCCIÓN DE PORTAFOLIO")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.code("""
# Definir pesos según nuestras preferencias como inversionistas
pesos <- c(NVDA = 0.50, TXN = 0.30, INTC = 0.20)  # 50%, 30%, 20%
cat("Composición del portafolio (nuestras preferencias como inversionistas):")
cat("• NVIDIA (NVDA): ", pesos["NVDA"] * 100, sep = "")
cat("• Texas Instruments (TXN): ", pesos["TXN"] * 100, sep = "")
cat("• Intel (INTC): ", pesos["INTC"] * 100, sep = "")
cat("• Total: ", sum(pesos) * 100, sep = "")

# Calcular retorno del portafolio
datos_portafolio <- datos_retornos %>%
  mutate(
    R_PORTAFOLIO = pesos["NVDA"] * R_NVDA + pesos["TXN"] * R_TXN + pesos["INTC"] * R_INTC
  )

# Modelo de regresión para el portafolio
modelo_portafolio <- analizar_regresion_completo(datos_portafolio$R_PORTAFOLIO, 
                                                 datos_retornos$R_NASDAQ, 
                                                 "Portafolio Diversificado")""")
    with col2:
        st.markdown("### 👉 Escogimos esta distribución específica (50% NVDA, 30% TXN, 20% INTC) porque representa el perfil de un inversionista balanceado que busca crecimiento pero  con  gestión de riesgo.")
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### <span style='color:#FF8C00'>INTERPRETACIÓN DE LA BETA DEL PORTAFOLIO:", unsafe_allow_html=True)
        st.markdown("##### Ecuación del portafolio: R_PORTAFOLIO,t = αp + βp × R_NASDAQ,t + εt β del portafolio: 1.4641")
        st.markdown("##### <span style='color:#FF8C00'>Interpretación:", unsafe_allow_html=True)
        st.markdown("##### • El portafolio es MÁS volátil que el mercado (βp > 1).")
        st.markdown("##### • Por cada 1% de movimiento del NASDAQ, el portafolio se moverá aproximadamente 1.46%.")
    with col1:
        st.code("""
cat("Ecuación del portafolio: R_PORTAFOLIO,t = αp + βp × R_NASDAQ,t + εt")
cat("β del portafolio: ", round(modelo_portafolio$beta, 4), sep = "")

cat("Interpretación:")
if(modelo_portafolio$beta > 1) {
  cat("• El portafolio es MÁS volátil que el mercado (βp > 1)")
} else if(modelo_portafolio$beta < 1) {
  cat("• El portafolio es MENOS volátil que el mercado (βp < 1)")
} else {
  cat("• El portafolio tiene la MISMA volatilidad que el mercado (βp = 1)")
}
cat("• Por cada 1% de movimiento del NASDAQ, el portafolio se moverá aproximadamente ", 
    round(modelo_portafolio$beta, 2), sep = "")""")
    
    # 1.7 B)
    st.markdown("# <span style='color:yellow'>📡 Punto 1.7 (B)</span>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### <span style='color:#FF8C00'>COMPOSICIÓN DEL RIESGO DEL PORTAFOLIO", unsafe_allow_html=True)
        st.markdown("##### • R² del portafolio: 71.51%")
        st.markdown("##### • Riesgo de mercado: 71.51%")
        st.markdown("##### • Riesgo específico: 28.49%")
        st.markdown("##### <span style='color:#FF8C00'>Interpretación:", unsafe_allow_html=True)
        st.markdown("##### • 71.5% del riesgo total del portafolio corresponde al riesgo de mercado.")
        st.markdown("##### • 28.5% puede atribuirse al riesgo específico del portafolio.")
        st.markdown("##### • La diversificación reduce el riesgo específico en comparación con las acciones individuales.")
    with col1:
        st.code(""" # COMPOSICIÓN DEL RIESGO DEL PORTAFOLIO
riesgo_mercado_p <- modelo_portafolio$r_cuadrado * 100
riesgo_especifico_p <- (1 - modelo_portafolio$r_cuadrado) * 100

cat("• R² del portafolio: ", round(riesgo_mercado_p, 2), sep = "")
cat("• Riesgo de mercado: ", round(riesgo_mercado_p, 2), sep = "")
cat("• Riesgo específico: ", round(riesgo_especifico_p, 2), sep = "")""")
        
    
    # 1.7 C)
    st.markdown("# <span style='color:yellow'>📡 Punto 1.7 (C)</span>", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>INTERVALO DE CONFIANZA 95% PARA RETORNO DEL PORTAFOLIO", unsafe_allow_html=True)
    st.markdown("### <span style='color:#FF8C00'>Datos proporcionado: Retorno del índice NASDAQ = 1.24%", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col2:
        st.markdown("##### <span style='color:#FF8C00'>Resultados para el portafolio:", unsafe_allow_html=True)
        st.markdown("##### • Retorno esperado: 1.8506%")
        st.markdown("##### • Límite inferior IC 95%: 1.7168%")
        st.markdown("##### • Límite superior IC 95%: 1.9843%")
        st.markdown("##### • Intervalo de confianza 95%: [1.7168%, 1.9843%]")
        st.markdown("##### <span style='color:#FF8C00'>Interpretación:", unsafe_allow_html=True)
        st.markdown("##### • Con 95% de confianza, el retorno del portafolio estará entre 1.717% y 1.984%.")
        st.markdown("##### • Cuando el NASDAQ tenga un retorno de 1.24%")
    with col1:
        st.code(""" # INTERVALO DE CONFIANZA 95% PARA RETORNO DEL PORTAFOLIO
cat("Dato proporcionado: Retorno del índice NASDAQ = 1.24%")
                
ic_portafolio <- predict(modelo_portafolio$modelo,
                         newdata = data.frame(retorno_mercado = 1.24),
                         interval = "confidence", level = 0.95)
                
cat("Resultados para el portafolio:\n")
cat("• Retorno esperado: ", round(ic_portafolio[1], 4), sep = "")
cat("• Límite inferior IC 95%: ", round(ic_portafolio[2], 4), sep = "")
cat("• Límite superior IC 95%: ", round(ic_portafolio[3], 4), sep = "")
cat("• Intervalo de confianza 95%: [", round(ic_portafolio[2], 4), "%, ", 
    round(ic_portafolio[3], 4), sep = ""))""")