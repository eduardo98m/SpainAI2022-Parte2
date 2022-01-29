import streamlit as st
import billboard
def task():
    text  = """
            La tarea consiste en hacerle  preguntas a nuestro modelo sobre esta lista lista de canciones.
            
            """
    st.markdown(text)
    chart = billboard.ChartData("hot-100")
    st.write(chart)