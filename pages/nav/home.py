import streamlit as st
import json
from streamlit_lottie import st_lottie

def show_home():
    # Título principal
    st.title("Bem-vindo ao Detector de Fake News 📰!")

    # Subtítulo
    st.subheader("Olá! Eu sou Thaleson Silva 👋")

    # Colunas que organizam a página
    col1, col2 = st.columns(2)

    # Animações
    with open("anims/anim1.json") as source:
        animacao_1 = json.load(source)

    with open("anims/anim3.json") as source:
        animacao_2 = json.load(source)

    # Conteúdo a ser exibido na coluna 1
    with col1:
        st_lottie(animacao_1, height=450, width=450)
        st.write("")
        st.markdown("""
            <h5 style='text-align: justify; line-height: 1.6;'>
                Este projeto de Detecção de Fake News é uma aplicação interativa que utiliza 
                inteligência artificial para identificar e classificar notícias como verdadeiras 
                ou falsas. O objetivo é promover uma leitura crítica e ajudar a combater a desinformação.
            </h5>
        """, unsafe_allow_html=True)

    # Conteúdo a ser exibido na coluna 2
    with col2:
        st.write("")
        st.markdown("""
            <h5 style='text-align: justify; line-height: 1.6;'>
                Bem-vindo ao sistema de Detecção de Fake News! 📰🚀
                Aqui, você pode inserir uma notícia e verificar sua veracidade utilizando 
                um modelo treinado para distinguir entre informações verdadeiras e falsas.
                Aproveite a tecnologia de IA para se manter bem informado!
            </h5>
        """, unsafe_allow_html=True)
        st_lottie(animacao_2, height=400, width=440)
