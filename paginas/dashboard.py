import streamlit as st

import plotly.express as px

import pandas as pd 

import numpy as np

from utils import gerar_chave

import src.eda as eda

base = pd.read_csv("./data/shopping_trends_updated.csv")

def dashboard():
        
    with st.sidebar:
        st.header("Filtros")
        
        # Filtro de Idade (Slider)
        age_min, age_max = st.slider(
            "Selecione a faixa etária:",
            min_value = base['Age'].min(),
            max_value = base['Age'].max(),
            value = (base['Age'].min(), base['Age'].max()),
            key = "age_slider"
        )
        
        # Filtro de Gênero (Multiselect)
        gender_options = base['Gender'].unique().tolist()
        selected_genders = st.multiselect(
            "Selecione os gêneros:",
            options = gender_options,
            default = gender_options,
            key = "gender_multiselect"
        )
        
        # Filtro de Localização (Dropdown)
        season_options = base['Season'].unique().tolist()
        selected_seasons = st.multiselect(
            "Selecione as estações:",
            options = season_options,
            default = season_options,
            key = "season_multiselect"
        )

    base_filtrada = base[
    (base['Age'].between(age_min, age_max)) &
    (base['Gender'].isin(selected_genders)) &
    (base['Season'].isin(selected_seasons))]

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

    st.plotly_chart(eda.grafico_idade(base_filtrada), key = gerar_chave(base, "grafico_idade"))

    col5, col6 = st.columns(2)

    with col5:

        st.plotly_chart(eda.grafico_generos(base_filtrada), key = gerar_chave(base, "grafico_generos"), use_container_width = True)

    with col6:

        st.plotly_chart(eda.grafico_media_genero(base_filtrada),key = gerar_chave(base, "grafico_media_genero"), use_container_width = True)
