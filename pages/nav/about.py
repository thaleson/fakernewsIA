import streamlit as st

def show_about():

    st.markdown("""
    <h1 style='color: #007BFF;'>Sobre o Projeto</h1>
    <p style='color: #FFFFFF;'>Este projeto visa detectar fake news utilizando técnicas de Processamento de Linguagem Natural (NLP) e aprendizado de máquina. O modelo foi treinado com notícias rotuladas como verdadeiras ou falsas para ajudar na identificação e combate à desinformação. 📰🤖</p>
    
    <h2 style='color: #007BFF;'>Funcionalidades:</h2>
    <p style='color: #FFFFFF;'> 
    Detecção em Tempo Real: O modelo pode processar e analisar textos rapidamente, classificando se a notícia é verdadeira ou falsa. 🕵️‍♂️🖥️<br>
    Porcentagem de Certeza: O aplicativo exibe a porcentagem de confiança da previsão, mostrando o quão seguro o modelo está em sua classificação. 📊🤖
    </p>

    <h2 style='color: #007BFF;'>Instruções de Uso:</h2>
    <p style='color: #FFFFFF;'> 
    1. Insira o texto ou notícia que deseja verificar.<br>
    2. Aguarde o processamento e obtenha a classificação do modelo (Verdadeira ou Falsa).<br>
    3. Confira a porcentagem de confiança associada à previsão e analise o resultado. 🖥️⚙️
    </p>

    <h2 style='color: #007BFF;'>Tecnologias Utilizadas:</h2>
    <p style='color: #FFFFFF;'> 
    Este aplicativo foi desenvolvido utilizando as seguintes tecnologias:<br>
    - Streamlit: Biblioteca para criação de interfaces web interativas usando Python.<br>
    - Scikit-learn: Utilizada para o treinamento dos modelos de classificação.<br>
    - NLTK e spaCy: Bibliotecas de NLP utilizadas para pré-processamento e análise de texto.<br>
    - Pandas: Usada para manipulação e análise de dados.<br>
    - TensorFlow/Keras: Utilizados para construir e treinar modelos de deep learning, incluindo LSTM e CNN para detecção de padrões complexos em textos. 🤖🧠
    </p>

    <h2 style='color: #007BFF;'>Desenvolvedor:</h2>
    <p style='color: #FFFFFF;'> 
    Este aplicativo foi desenvolvido por Thaleson Silva. Sou entusiasta de inteligência artificial e NLP, e este projeto busca contribuir para a verificação de fatos e o combate à desinformação. 🚀<br>
    Agradecemos seu uso e ficamos abertos a feedbacks para melhorar o sistema. 🙌
    </p>

    <h2 style='color: #007BFF;'>Como o Modelo Foi Treinado:</h2>
    <p style='color: #FFFFFF;'> 
    O modelo de detecção de fake news foi treinado com um conjunto de dados de notícias rotuladas como verdadeiras ou falsas, seguindo estas etapas:</p>
    
    <h3 style='color: #007BFF;'>1. Pré-processamento dos Dados:</h3>
    <p style='color: #FFFFFF;'> 
    O texto foi tokenizado, e foram removidas stop words e pontuação. Abaixo está um exemplo de código de pré-processamento com NLTK:
    </p>

    ```python
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import string

    # Função para pré-processamento de texto
    def preprocess_text(text):
        stop_words = set(stopwords.words('portuguese'))
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha() and word not in stop_words]
        return tokens
    ```

    <h3 style='color: #007BFF;'>2. Treinamento do Modelo:</h3>
    <p style='color: #FFFFFF;'> 
    Modelos como Regressão Logística, Random Forest e LSTM foram treinados utilizando vetores TF-IDF para representar o texto. O código a seguir mostra como os dados foram preparados e o modelo foi treinado:
    </p>

    ```python
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    # Vetorização e divisão dos dados
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(text_data)
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Treinamento de um modelo de Regressão Logística
    model = LogisticRegression()
    model.fit(X_train, y_train)
    ```

    <h3 style='color: #007BFF;'>3. Avaliação e Ajuste:</h3>
    <p style='color: #FFFFFF;'> 
    Após o treinamento, o modelo foi avaliado usando métricas como precisão e recall. A seguir, realizamos ajustes no modelo para melhorar a acurácia geral.
    </p>

    <p style='color: #FFFFFF;'> 
    O código acima resume o processo de pré-processamento, treinamento e avaliação do modelo. O uso de técnicas de NLP e aprendizado de máquina permite ao modelo identificar padrões em textos e detectar notícias falsas de forma eficaz.
    </p>
    """, unsafe_allow_html=True)

