import streamlit as st
import billboard
def task():
    text  = """
            La tarea consiste en hacer cosas con la lista billboard 
            
            """
    st.markdown(text)
    chart = billboard.ChartData("hot-100")
    st.write(chart)