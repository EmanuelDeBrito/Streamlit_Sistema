# Importações
import streamlit as st # Importando o streamlit com o apelido de st
from PIL import Image # Importando Image da biblioteca de imagem PILLOW
import requests # Importando a biblioteca requests
import streamlit_lottie # Importando o lottie
from streamlit_lottie import st_lottie # do lottie importa o st_lottie


# Função para transformar os links json do lottie em animações
def lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Links dos json
banana = "https://assets6.lottiefiles.com/private_files/lf30_vuxs5lpt.json"
rodolfo = "https://assets1.lottiefiles.com/packages/lf20_7aq7s6rs.json"
oswaldo = "https://assets10.lottiefiles.com/private_files/lf30_WVVTq8.json"
paulo = "https://assets10.lottiefiles.com/packages/lf20_2znxgjyt.json"
jonas = "https://assets8.lottiefiles.com/packages/lf20_2nbubmkc.json"
jussimar = "https://assets2.lottiefiles.com/packages/lf20_rgrylcip.json"
wellington = "https://assets5.lottiefiles.com/packages/lf20_E0GQM0.json"

# Transformando os links json em animações
banana_json = lottieurl(banana)
rodolfo_json = lottieurl(rodolfo)
oswaldo_json = lottieurl(oswaldo)
paulo_json = lottieurl(paulo)
jonas_json = lottieurl(jonas)
jussimar_json = lottieurl(jussimar)
wellington_json = lottieurl(wellington)

# Um titulo do BananaWeb
st.title('BananaWeb')

# colocando um texto em formato de linguagem
codigo = ''' def bananinha():
    print("Informações Pessoais")
    informacoes = [{'Nome': 'Augusto Fabiano Abranches'}
    {'Idade': '??'}
    {'Vugo': 'Bananinha'}
    {'Raça': 'Alienigina'}
    {'Linguagem': 'Mestre do Banco de Dados e Arduíno'}]
'''

# Transforamando esse código de cima em um st.code para ficar bonito na página
st.code(codigo, language="python")

# Atribuindo a uma variavel o caminho da imagem
programacao = Image.open(r"C:\Users\danil\Downloads\dev.jpg")

# Colocando a imagem na tela
st.image(programacao)

# Criando colunas
col1, col2, col3 = st.columns(3)

# Na coluna 1
with col1:
    # Um header
    st.header('BananaWeb')
    # Um texto
    st.write('Como foi pedido para fazer um sisteminha pensei em fazer um simples Website sobre o banana')

# Na coluna 2
with col2:
    # Um header
    st.header('Aulas')
    # Um texto
    st.write('As aulas ajudam muito professor apesar de serem um pouco loucas elas ajudam bastante, pega leve no TCC =)')

# Na coluna 3
with col3:
    # Um header
    st.header('Agradecimentos')
    # Um texto
    st.write('Agradeço a todos professores pelas máterias passadas que foram muito importantes para o crescimento')

# Colocando mais um header
st.header('Professores')

# Fazendo tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Bananinha", "Jonas", "Jussimar",
                                                    "Oswaldo", "Paulo", "Rodolfo", "Wellington"]) # Quebrei a linha

# Agora vou fazer para cada tab uma descrição
with tab1:
    st.header('Augusto')
    st.write('Apesar da aula ser um pouco maluca as máterias são sempre dadas com maestria pelo professor sempre sendo muito engraçadas e utéis')
    st_lottie(banana_json, key='Banana')
with tab2:
    st.header('Jonas')
    st.write('Mestre do Design, nos passou muitas ferramentas espetaculares e faz muita falta no 2 e no 3 módulo aulas de design')
    st_lottie(jonas_json, key='Jonas')
with tab3:
    st.header('Jussimar')
    st.write('Apesar dos labs não ajudarem muito nos ensinou bastante de react e nos ajudou a pensar mais em mobile')
    st_lottie(jussimar_json, key='Jussimar')
with tab4:
    st.header('Oswaldo')
    st.write('Essa aqui nem precisa falar, muitos dizem que o Oswaldo foi o primeiro humano a fazer um sistema na face da terra')
    st_lottie(oswaldo_json, key='Oswaldo')
with tab5:
    st.header('Paulo')
    st.write('Professor Minigênio, mestre de pandas e análises de sistema, além de ser um orientador excepcional')
    st_lottie(paulo_json, key='Paulo')
with tab6:
    st.header('Rodolfo')
    st.write('Mestre do Php, sempre explica as máterias muito bem e ajuda bastante em dúvidas e ideias')
    st_lottie(rodolfo_json, key='Rodolfo')
with tab7:
    st.header('Mestre Yoda')
    st.write('Esse aqui é um gênio incompreendido pela sociedade, melhor amigo do sapinho')
    st_lottie(wellington_json, key='Wellington')
