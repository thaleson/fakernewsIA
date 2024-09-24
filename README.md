# 📰 Fake News Detection with NLP & Machine Learning 🔍

Bem-vindo ao projeto **Fake News Detection**! Este aplicativo usa técnicas de **Processamento de Linguagem Natural (NLP)** e **Machine Learning** para detectar se uma notícia é verdadeira ou falsa.

## 📋 Descrição do Projeto

Este projeto utiliza um **modelo de classificação** treinado com dados reais de notícias para prever se uma notícia é verdadeira ou uma fake news. O modelo foi construído com base em técnicas de **NLP** usando **TF-IDF** para vetorização do texto e um **classificador de machine learning**.

A aplicação foi desenvolvida utilizando **Streamlit** para fornecer uma interface web interativa.

## 📊 Funcionalidades

- **Previsão de Fake News**: O modelo analisa uma notícia e retorna se é verdadeira ou falsa.
- **Interface interativa**: O aplicativo é fácil de usar, permitindo que o usuário insira qualquer texto e obtenha uma resposta imediata.
- **Indicador de confiança**: Mostra uma mensagem com uma breve explicação sobre a acurácia do modelo.
- **Mensagens dinâmicas**: Durante a análise da notícia, há feedback visual de carregamento.

---

## 🚀 Começando

Estas instruções te guiarão na instalação do projeto e em como rodá-lo na sua máquina.

### 📦 Pré-requisitos

- **Python 3.8 ou superior** deve estar instalado em seu sistema.
- **pip** para instalação dos pacotes necessários.

### 🔧 Instalação

#### 1. Clone o repositório:

```bash
git clone https://github.com/thaleson/fakernewsIA.git
```

#### 2. Acesse o diretório do projeto:

```bash
cd fakernewsIA
```

#### 3. Crie um ambiente virtual (opcional, mas recomendado):

Para Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Para Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### 4. Instale as dependências:

```bash
pip install -r requirements.txt
```

### ▶️ Executando o Projeto

Após instalar as dependências, você pode rodar o aplicativo localmente usando o **Streamlit**. Execute o seguinte comando no terminal:

```bash
streamlit run main.py
```

Abra o navegador no endereço `http://localhost:8501` para acessar a interface do aplicativo.

---

## 📂 Estrutura do Projeto

```bash
fakernewsIA/
│
├── models/                  # Modelos e vetorizadores salvos
│   ├── modelo_fake_news.pkl  # Modelo de detecção de fake news
│   └── tfidf_vectorizer.pkl  # Vetorizador TF-IDF treinado
│
├── pages/                   # Páginas secundárias do Streamlit
│   ├── home.py              # Página inicial
│   ├── about.py             # Sobre o projeto
│   └── predict.py           # Página de previsão
│
├── main.py                  # Arquivo principal da aplicação Streamlit
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação do projeto
└── .gitignore               # Arquivos a serem ignorados pelo Git
```

---

## ⚙️ Tecnologias Utilizadas

- **Python** 🐍
- **Streamlit**: Framework para criar a interface web interativa.
- **Scikit-learn**: Biblioteca de machine learning utilizada para construir o classificador.
- **NLP (TF-IDF)**: Para processar e vetorização de texto.

---

## 📈 Modelo Utilizado

O modelo utilizado neste projeto é baseado em **machine learning** usando **TF-IDF** para transformar o texto e um classificador que faz a previsão se a notícia é falsa ou verdadeira.

O processo de treinamento foi feito utilizando dados reais de notícias e aplicando técnicas de **classificação supervisionada**.

---

## 🖥️ Compatibilidade

Este projeto é compatível com os seguintes sistemas operacionais:

- **Windows** 🪟
- **Linux** 🐧
- **MacOS** 🍎

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhoria, fique à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## 📬 Contato

Desenvolvido por **Thaleson Silva**. Para mais informações, entre em contato:

- [LinkedIn](https://www.linkedin.com/in/thaleson-silva-9298a0296/)
- [Email](mailto:thaleson19@hotmail.com)

---

## ⚠️ Aviso

Este projeto tem fins educacionais e o modelo não deve ser utilizado como única fonte para determinar a veracidade de notícias. O modelo tem uma acurácia aproximada de **72%** e pode não ser 100% preciso em todos os casos.



