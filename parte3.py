import streamlit as st

def parte3():
    st.markdown("# <span style='color:yellow'>📊 Parte III: Ejemplos CFA</span>", unsafe_allow_html=True)
    st.markdown("""
# 📘 Ejemplo 15 – Estimación del beta de Westport Innovations

Se calcula el **beta** de las acciones de Westport para medir qué tan sensibles son frente a los movimientos del mercado.  
Para ello se comparan los excesos de retorno de la acción con los excesos de retorno del mercado.  

**Variable endógena (dependiente):** (R − RF), exceso de retorno de la acción.  
**Variable exógena (independiente):** (RM − RF), exceso de retorno del mercado.  

---

# 📘 Ejemplo 16 – Relación entre ROIC–WACC y la valoración de empresas

Se analiza cómo la diferencia entre la **rentabilidad del capital invertido (ROIC)** y el **costo de capital (WACC)** ayuda a explicar el valor de la empresa respecto a su capital invertido (EV/IC) en compañías del sector alimentario.  

**Variable endógena:** EV/IC (ratio de valor de la empresa sobre capital invertido).  
**Variable exógena:** Spread (ROIC − WACC).  

---

# 📘 Ejemplo 17 – Pronósticos de inflación

Se estudia si las predicciones de inflación hechas por expertos son **insesgadas**, es decir, si realmente logran anticipar con precisión la inflación observada en la práctica.  

**Variable endógena:** Inflación real observada.  
**Variable exógena:** Pronóstico de inflación.  

---

# 📘 Ejemplo 18 – Evaluación de desempeño del fondo Dreyfus Appreciation

Se examina si el fondo logra generar **rendimientos superiores al mercado ajustados por riesgo**, utilizando el modelo CAPM para identificar si existe un “alfa” positivo.  

**Variable endógena:** Exceso de retorno del fondo (Ri − RF).  
**Variable exógena:** Exceso de retorno del mercado (RM − RF).  

---

# 📘 Ejemplo 19 – Predicción del valor de empresa (EV/IC)

Se usa la regresión del Ejemplo 16 para predecir la relación entre el **valor de la empresa y su capital invertido (EV/IC)** dado un diferencial específico entre ROIC y WACC, incluyendo un intervalo de predicción.  

**Variable endógena:** EV/IC (ratio de valor de la empresa sobre capital invertido).  
**Variable exógena:** Spread (ROIC − WACC).  
""")
