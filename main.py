import streamlit as st
from streamlit_option_menu import option_menu
import pages.nav.home as home
import pages.nav.about as about
import json
from streamlit_lottie import st_lottie

# Configuração da página
st.set_page_config(
    page_title='Detector de Fake News 📰',
    page_icon='📰',
    layout='wide'
)

# Aplicar estilos de CSS à página (se houver)
try:
    with open("static/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Arquivo de estilo CSS não encontrado!")

# Função para carregar animação JSON
def load_lottie(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Menu de navegação com ícones
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",  # required
        options=["Home", "Sobre o Projeto", "Previsão"],  # required
        icons=["house", "info-circle", "check-circle"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

    # Badges
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Navegação
if selected == "Home":
    home.show_home()
elif selected == "Sobre o Projeto":
    about.show_about()
elif selected == "Previsão":
    from pages.nav.predict import show_predict
    show_predict()
