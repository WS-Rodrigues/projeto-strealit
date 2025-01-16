import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meu sistema Streamlit",
    page_icon="✔",
    layout="wide"
    )

lateral = st.sidebar
data = lateral.date_input("Selecione a data")

st.title("Minha primeira aplicação")
st.header("Seções")
st.write("Um texto utilizando write :smile:")
st.subheader("Sub seção")
st.text("Elemento para apenas texto")

st.subheader("Markdown")
st.markdown("""
#   Título primeiro nível
##  Título segundo nível
-   Item 1
-   Item 2
-   Item 3
            """)
st.subheader("Códigos")
st.code("""
nome = 'Wendel'
print(nome)
        """)

st.header("Elementos de entrada de dados - parte 1")
st.subheader("st.text_input")
nome = st.text_input("Digite o seu nome: ")
st.text(nome)

st.subheader("st.number_input")
numero = st.number_input("Entre comum número")

st.header("Elementos de entrada de dados - parte 2")
st.subheader("st.date_input")
data = st.date_input("Entre com uma data: ",
                     key="input_data",
                     format="DD/MM/YYYY")
st.text(type(data))
st.text(data.strftime(format="%d/%m/%Y"))

botao = st.button("Clique aqui para cadastrar",
          key= "btn_cadastrar")
if botao:
    st.write("O Botão foi clicado!")
    st.write(f"Nome: {nome}")
    st.write(f"Data: {data.strftime(format='%d/%m/%Y')}")

st.header("Elementos de entrada de dados - parte 3")
st.subheader("st.selectbox")
cor = st.selectbox("Escolha uma cor:", 
                   ["Vermelho", "Azul", "Verde"],
                   key="sb_cor" )
st.write(cor)

st.subheader("st.multiselect")
cores = st.multiselect("Selecione as cores:", 
                    ["Vermelho", "Azul", "Verde"])

st.write(cores)

st.subheader("st.radio")
opcao = st.radio("Escolha uma opção: ",
                 ["Masculino", "Feminino"])

st.text(opcao)

st.header("Elementos de entrada de dados - parte 4")
st.subheader("st.checktbox")
aceite = st.checkbox("Eu aceito os termos.")
st.text(aceite)

st.header("Elementos de status")
boton = st.button("Clique aqui para ver o status!")

if boton:
    st.success("Cadastro realizado com sucesso!", icon="👍")
    st.snow()


st.header("Elementos de Análise de dados - parte 1")

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

dados = carregar_dados()
st.session_state["dados"] = dados
st.session_state["data"] = data    

tabela_dados = st.data_editor(dados)
carregar = st.button("Carregar dados!")

st.header("Elementos de Análise de dados - parte 2(Visualização dos dados.)")

mostrar_grafico = st.toggle("Mostrar gráficos")

contagem_municipios = dados["municipio"].value_counts()
st.dataframe(contagem_municipios)

if mostrar_grafico:
    st.bar_chart(contagem_municipios)
    
st.image("imagem.png")
st.audio("12-audio.mp3")

