import streamlit as st

import plotly.express as px

import pandas as pd 

import numpy as np


base = pd.read_csv("./data/shopping_trends_updated.csv")

base = base.drop(columns = "Frequency of Purchases")

def dashboard():

    st.title("📊 Dashboard de Tendências do Mercado de Vestuário")
