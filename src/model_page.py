import streamlit as st

def model():

    st.write("""
    El modelo que vamos a utilizar es el:
    ```
    sentence-transformers/paraphrase-multilingual-mpnet-base-v2
    ```

    Y no les voy a dejar escojer otro porque **no se cambia lo que no esta roto.**
    """)

    model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
   