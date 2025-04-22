# %%

# Dicionario dos dados
# 📌 Customer ID - Identificador único para cada cliente.
# 📌 Age - Idade do cliente.
# 📌 Gender - Gênero do cliente (Masculino/Feminino).
# 📌 Item Purchased - Item comprado pelo cliente.
# 📌 Category - Categoria do item comprado.
# 📌 Purchase Amount (USD) - Valor da compra em dólares (USD).
# 📌 Location - Local onde a compra foi realizada.
# 📌 Size - Tamanho do item comprado.
# 📌 Color - Cor do item comprado.
# 📌 Season - Estação do ano em que a compra foi realizada.
# 📌 Review Rating - Avaliação dada pelo cliente para o item comprado.
# 📌 Subscription Status - Indica se o cliente tem uma assinatura (Sim/Não).
# 📌 Shipping Type - Tipo de envio escolhido pelo cliente.
# 📌 Discount Applied - Indica se um desconto foi aplicado à compra (Sim/Não).
# 📌 Promo Code Used - Indica se um código promocional foi utilizado na compra (Sim/Não).
# 📌 Previous Purchases - Número de compras anteriores feitas pelo cliente.
# 📌 Payment Method - Método de pagamento mais utilizado pelo cliente.
# 📌 Frequency of Purchases - Frequência com que o cliente realiza compras (ex.: Semanalmente, Quinzenalmente, Mensalmente).

# %%

import pandas as pd 

import plotly.express as px

import numpy as np

# %% 

base = pd.read_csv("./data/shopping_trends_updated.csv")

base.head()

# %%

base.info()

# %%

clt_total = base["Customer ID"].unique().__len__()

clt_total

# %%

base["Purchase Amount (USD)"] = base["Purchase Amount (USD)"].astype(float)

# %%

vnd_totais = round((base["Purchase Amount (USD)"].sum()), 2)

vnd_formatado = f"{vnd_totais:,.2f}"

vnd_formatado

# %%

tck_medio = round((vnd_totais/clt_total), 2)

tck_medio

# %%

avl_media = round(((base["Review Rating"].sum())/clt_total), 2)

avl_media

# %%
