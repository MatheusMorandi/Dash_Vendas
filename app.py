import pandas as pd 

import numpy as np

import streamlit as st

from streamlit_option_menu import option_menu

import plotly.express as px


base = pd.read_csv("./data/shopping_trends_updated.csv")

base = base.drop(columns = "Frequency of Purchases")

# Configuração da página
st.set_page_config(
    page_title="Dash de Vendas", 
    layout="wide",
    page_icon="🛒"
)

# CSS personalizado
st.markdown("""
    <style>
        /* Centraliza o título h1 */
        [data-testid="stSidebar"] h1 {
            text-align: center;
            width: 100%;
            margin: 0  !important;
        }

        /* Centraliza o menu */
        .st-emotion-cache-16txtl3 {
            margin: auto;
            justify-content: center;
        }

        /* Ajusta a logo */
        .stSidebar img {
            display: block;
            margin: 0 !important;
        }

        /* Remove espaçamento extra */
        [data-testid="stSidebarNav"] {
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("./img/logo_dash.png")

with st.sidebar:

    st.title("Menu")
    
    selected = option_menu(
        menu_title = None,
        options = ["Sobre", "Dashboard", "Contato"],
        icons = ["info-square-fill", "bar-chart-fill", "person-vcard-fill"],
        default_index = 0,
        styles = {
            "container": {"padding": "0!important"},
            "nav-link": {"font-size": "16px",
                        "--hover-color" : "#1E90FF"},
            "nav-link-selected" : {"background-color" : "#1E3A8A"},
            "menu-icon": {"display": "none"}  
        }
    )
