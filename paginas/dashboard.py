import streamlit as st

import plotly.express as px

import pandas as pd 

import numpy as np

from utils import gerar_chave

import src.eda as eda

base = pd.read_csv("./data/shopping_trends_updated.csv")

def dashboard():

    st.title("📊 Análise das Tendências do Mercado de Vestuário")        

    st.subheader("Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric("Clientes Totais: ", eda.clt_total) 

    with col2:

        st.metric("Total em Vendas (USD)", eda.vnd_formatado)

    with col3:

        st.metric("Ticket Médio (USD)", eda.tck_medio) 

    with col4:

        st.metric("Avaliação média de reviews", eda.avl_media)

    st.subheader("Análise Demográfica")

    st.plotly_chart(eda.grafico_idade(base), key = gerar_chave(base, "grafico_idade"))

    col5, col6 = st.columns(2)

    with col5:

        st.plotly_chart(eda.grafico_generos(base), key = gerar_chave(base, "grafico_generos"), use_container_width = True)

    with col6:

        st.plotly_chart(eda.grafico_media_genero(base),key = gerar_chave(base, "grafico_media_genero"), use_container_width = True)

    st.plotly_chart(eda.grafico_top_estado(base), key = gerar_chave(base, "grafico_top_estado"))

    st.subheader("Performance de Vendas")