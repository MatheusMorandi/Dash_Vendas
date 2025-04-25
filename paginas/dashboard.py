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

    col1, col2, col3, col4, col5 = st.columns(5, gap = "small")

    with col1:

        st.metric("Clientes Totais: ", eda.clt_total) 

    with col2:

        st.metric("Total em Vendas (USD)", eda.vnd_formatado)

    with col3:

        st.metric("Ticket Médio (USD)", eda.tck_medio) 

    with col4:

        st.metric("Avaliação Média", eda.avl_media)
    
    with col5:

        st.metric("Clientes Inscritos ", eda.tx_assinatura)

    st.subheader("Análise Demográfica")

    st.plotly_chart(eda.grafico_idade(base), key = gerar_chave(base, "grafico_idade"))

    col6, col7 = st.columns(2)

    with col6:

        st.plotly_chart(eda.grafico_generos(base), key = gerar_chave(base, "grafico_generos"), use_container_width = True)

    with col7:

        st.plotly_chart(eda.grafico_media_genero(base),key = gerar_chave(base, "grafico_media_genero"), use_container_width = True)

    st.plotly_chart(eda.grafico_top_estado(base), key = gerar_chave(base, "grafico_top_estado"))

    st.subheader("Performance de Vendas")

    col8, col9 = st.columns(2)

    with col8:

        st.plotly_chart(eda.grafico_categorias(base), key = gerar_chave(base, "grafico_categorias"), use_container_width = True)

    with col9:

        st.plotly_chart(eda.grafico_estacoes(base), key = gerar_chave(base, "grafico_estacoes"), use_container_width = True)
    
    st.plotly_chart(eda.grafico_itens(base), key = gerar_chave(base, "grafico_itens"))

    st.subheader("Comportamento do Cliente")

    col10, col11 = st.columns(2)

    with col10:

        st.plotly_chart(eda.grafico_pagamentos(base), key = gerar_chave(base, "grafico_pagamentos"), use_container_width = True)

    with col11:

        st.plotly_chart(eda.grafico_media_pag(base), key = gerar_chave(base, "grafico_media_pag"), use_container_width = True)
    
    st.subheader("Análise de Descontos e Promoções")

    col12, col13 = st.columns(2)

    with col12:

        st.plotly_chart(eda.grafico_fretes(base), key = gerar_chave(base, "grafico_fretes"), use_container_width = True)

    with col13:

        st.plotly_chart(eda.grafico_desconto(base), key = gerar_chave(base, "grafico_desconto"), use_container_width = True)
    
    footer_css = """
        <style>
        .footer-container {
            position: relative;
            margin-top: auto;  
            padding: 20px;
            background-color: transparent;
        }

        
        .footer {
            text-align: center;
            color: rgba(128, 128, 128, 0.5);
            font-size: 0.9em;
            border-top: 1px solid rgba(128, 128, 128, 0.2);
            padding-top: 15px;
        }

        
        .spacer {
            height: 50px;
        }
        </style>
        """

        
    footer_html = """
        <div class="footer-container">
            <div class="footer">
               Desenvolvido por Matheus Morandi © 2024 
            </div>
        </div>
        """

    
    st.markdown(footer_css, unsafe_allow_html=True)

    st.markdown(footer_html, unsafe_allow_html=True)