import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Servicio de prediccion de estado psicologico')
    st.write('**Por favor, seleccione el tipo de datos a predecir**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('Predicción mediante conexion a cuenta en red social', 'Prediccion mediante texto ingresado manualmente'), 
                      index=0, 
                      key='option')
    
    if st.button('Comenzar analisis'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Predicción mediante conexion a cuenta en red social':
        switch_page("predict_twitter")
    elif opcion == 'Prediccion mediante texto ingresado manualmente':
        switch_page("pred_text")
  

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2