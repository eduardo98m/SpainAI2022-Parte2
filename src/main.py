
import streamlit as st
import streamlit.components.v1 as components

# Importamos las paginas
from home_page import home
from task_page import task
from page_sidebar import sidebar
from model_page import model


def main():
    # Configuraciones de nuestra pagina web
    st.set_page_config(
        page_title="Mira mamá mi propio modelo de ML",
        page_icon="⚙️",
        layout="wide",
        initial_sidebar_state="expanded",
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

    pages_mapper = {

        "Inicio ⚙️⚡":home,
        "La Tarea 📔":task,
        "El Señor Modelo 🗘":model,

    }

    #Distintas paginas!!!#

    pages_list = list(pages_mapper.keys())


    if 'current_page' not in st.session_state:
        st.session_state.current_page = pages_list[0]

    current_page, st.session_state.current_page = sidebar(pages_list)

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

    st.title(st.session_state.current_page)
    
    pages_mapper[current_page]()
    

if __name__ == "__main__":
    main()