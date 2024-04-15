import streamlit as st
import pandas as pd
from utils import predict_Text


# Título de la aplicación
st.title('Analisis y prediccion de tendencias suicidas en base a Texto')
st.image('suicidio_texto.jpeg', caption='No estas solo desgraciado!', use_column_width=True)

# Creamos un uploader para que el usuario pueda subir un archivo
archivo_subido = st.file_uploader("Sube tu archivo de texto aquí", type=["txt"])

if archivo_subido is not None:
    # leer contenido como un string
    contenido = archivo_subido.read().decode('utf-8')

    # Mostramos el contenido en la aplicación
    st.write("Contenido del texto:")
    st.write(contenido)


    # Sección para realizar la predicción
    st.subheader('Analizar el texto')

    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Comenzar analisis'):
        # Realizar la predicción utilizando las columnas seleccionadas
        predicted_values = predict_Text(contenido)

        # Mostrar los resultados de la predicción
        st.success('Se ha completado el analisis')
        st.write('Los resultados del analisis del texto proporcionado son:')
        st.write(predicted_values)


        # Convertimos la cadena de texto a bytes, necesario para la función de descarga
        texto_a_descargar = predicted_values.encode('utf-8')

        # Creamos un botón de descarga para el archivo de texto
        st.subheader('Si lo deseas puedes descargar el resultado del analisis:')
        st.download_button(
            label="Descargar como TXT",
            data=predicted_values,
            file_name="analisis_descargable.txt",
            mime="text/plain"
        )
