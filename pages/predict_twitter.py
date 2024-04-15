import streamlit as st
import pandas as pd
from utils import predict_Link
from utils import obtener_datos_desde_api
# Título de la aplicación
st.title('Copia la url del perfil que quieres predecir')
st.image('suicidio_texto.jpeg', caption='No estas solo desgraciado!', use_column_width=True)
enlace = st.text_input("Ingrese el enlace para obtener datos")

if st.button("Obtener datos y hacer predicción"):
    if enlace:
        # Obtener datos desde la API
        datos = obtener_datos_desde_api(enlace)
        
        # Verificar si se obtuvieron datos
        if datos:
            # Hacer la predicción con el modelo
            resultado_prediccion = predict_Link(datos)
            
            # Mostrar el resultado de la predicción
            st.write("Resultado de la predicción:")
            st.write(resultado_prediccion)
        else:
            st.warning("No se pudieron obtener datos de la API")
    else:
        st.warning("Por favor ingrese un enlace válido")
