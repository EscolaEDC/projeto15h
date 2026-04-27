import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    data = pd.read_excel('Base.xlsx', sheet_name='Base')
    title = "Dashboard de Vendas"
    st.set_page_config(page_title=title, layout="wide")
    st.title(title)

    anos = data['Ano'].unique()
    paises = data['País'].unique()

    filtro_ano = st.sidebar.selectbox("Selecione o Ano:", options=["Todos"] + sorted(anos), index=0)
    filtro_pais = st.sidebar.selectbox("Selecione o País:", options=["Todos"] + sorted(paises), index=0)

    data_filtrada = data.copy()
    if filtro_ano != "Todos":
        data_filtrada = data_filtrada[data_filtrada['Ano'] == filtro_ano]
    if filtro_pais != "Todos":
        data_filtrada = data_filtrada[data_filtrada['País'] == filtro_pais]

main()
