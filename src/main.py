
import streamlit as st
import streamlit.components.v1 as components


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

#
components.html(
    f"""
        <p>{st.session_state.current_page }</p>
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
    """,
    height=0
)

#Distintas paginas!!!#

pages = ["Inicio ⚙️⚡",
         "La Tarea 📔",
         "El Señor Modelo 🗘",
         ]

st.session_state.current_page = st.sidebar.radio(
    "",
    pages)

if 'current_page' not in st.session_state:
    st.session_state.current_page = pages[0],
# Funciones

st.title("Hola mama mira mi propio modelo de ML")