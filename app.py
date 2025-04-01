import pandas as pd 

import numpy as np

import streamlit as st

import plotly.express as px


base = pd.read_csv("./data/shopping_trends_updated.csv")

base = base.drop(columns = "Frequency of Purchases")

# Configuração da página
st.set_page_config(page_title = "Meu Dashboard", 
                layout="wide")

# Título
st.title("Dashboard de Tendências do Mercado de Vestuário")

