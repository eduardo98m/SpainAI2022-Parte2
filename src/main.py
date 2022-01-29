
import streamlit as st


# Configuraciones de nuestra pagina web


st.set_page_config(
    page_title="Mira mamá mi propio modelo de ML",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "https://github.com/eduardo98m/SpainAI2022-Parte2",
    }
)

# Removal of the default Streamlit Main Menu and footer
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Funciones

st.title("Hello World")