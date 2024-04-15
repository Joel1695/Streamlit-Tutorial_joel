import streamlit as st
import numpy as np
def predict_Link(data):
    #api porcesa y descarga informacion del link (tweets de el ultimo mes del usuario)
    #se prosesan los texto y se vectorizan 
    # Cargar el modelo previamente entrenado para predecir probabilidad de tendecias suicidas 
    # model = load_model(ubicaciondel modelo)
    # Realizar la predicción con los datos proporcionados
    porcentaje = np.random.randint(1,101)
    if porcentaje > 50 :
        texto = 'Teniendo en cuenta el resultado del analisis sobre el texto seleccionado recomendamos que se busque asistencia profesional.'
    elif porcentaje < 50 :
        texto = 'Teniendo en cuenta el resultado del análisis sobre el texto seleccionado no parece necesario buscar asistencia profesional, no obstante es conveniente estar alerta ante signos de ansiedad o depresión crónica'
    predictions = f"La probabilidad de que esta persona tenga tendencias suicidas es del {porcentaje}%. \n {texto}"
    return predictions

def predict_Text(text):
    #Se procesan el texto y se vectorizan.
    # Cargar el modelo previamente entrenado para predecir probabilidad de tendecias suicidas 
    # model = load_model(ubicaciondel modelo)
    # Realizar la predicción con los datos proporcionados
    porcentaje = np.random.randint(1,101)
    if porcentaje > 50 :
        texto = 'Teniendo en cuenta el resultado del analisis sobre el texto seleccionado recomendamos que se busque asistencia profesional.'
    elif porcentaje < 50 :
        texto = 'Teniendo en cuenta el resultado del análisis sobre el texto seleccionado no parece necesario buscar asistencia profesional, no obstante es conveniente estar alerta ante signos de ansiedad o depresión crónica'
    predictions = f"La probabilidad de que esta persona tenga tendencias suicidas es del {porcentaje}%. \n {texto}"
    return predictions



# Función para interactuar con la API
def obtener_datos_desde_api(link):
    #api porcesa y descarga informacion del link (tweets de el ultimo mes del usuario)
    #se deja la infomacion en el formato correspondiente para su vectorizacion
    return link