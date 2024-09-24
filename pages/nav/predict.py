import streamlit as st
import joblib
import time

def show_predict():
    st.subheader("Previsão de Fake News 📰🔍")
    
    # Carregar o modelo e o vetor TF-IDF
    model = joblib.load('models/modelo_fake_news.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

    # Entrada de texto para a notícia
    user_input = st.text_area("Digite a notícia aqui:", height=150)

    # Função para prever a notícia
    def predict_fake_news(text):
        text_tfidf = vectorizer.transform([text])
        prediction = model.predict(text_tfidf)
        return prediction[0]  # Retorna 0 ou 1

    # Função para verificar se o texto parece ser uma notícia
    def is_news(text):
        # Verifica se o texto contém palavras-chave e tem um tamanho razoável
        keywords = ["notícia", "reportagem", "estudo", "pesquisa", "análise", "informação", "fatos"]
        return (len(text.split()) > 5 and any(keyword in text.lower() for keyword in keywords))

    # Botão de prever
    if st.button('Verificar'):
        if user_input:
            if not is_news(user_input):
                st.warning("⚠️ **Por favor, insira um texto que seja uma notícia. O modelo foi treinado para verificar informações jornalísticas.**")
            else:
                # Adiciona o efeito de "analisando"
                with st.spinner('Analisando a notícia... 🔍'):
                    time.sleep(2)  # Simula um tempo de carregamento
                    result = predict_fake_news(user_input)
                
                # Exibe o resultado da previsão
                if result == 0:
                    st.error("🛑 **Esta informação provavelmente é: Fake News!**")
                else:
                    st.success("✔️ **Esta informação provavelmente é: Verdadeira!**")
        else:
            st.warning("Por favor, insira um texto antes de verificar!")

    # Aviso sobre a precisão do modelo
    st.markdown(""" 
        <div style='background-color: #FFFF00; padding: 10px; border-radius: 5px; color: black; font-weight: bold;'>
            <p style='font-size: 14px;'>
                🔍 Este modelo apresenta uma acurácia de aproximadamente 72% em suas previsões. 
                Lembre-se de que esta ferramenta é para fins de estudo e deve ser utilizada com cautela.
            </p>
        </div>
    """, unsafe_allow_html=True)
