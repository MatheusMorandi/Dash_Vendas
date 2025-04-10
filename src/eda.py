# %%

# Link do dataset https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset

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

base = pd.read_csv("../data/shopping_trends_updated.csv")

base.head()

# %%

base.info()

# %%

base = base.drop(columns = "Frequency of Purchases")

base.head()
# %%

itens_qntd =  base["Item Purchased"].agg("sum")

itens_qntd

# %%

itens_valor = base.groupby("Item Purchased")["Purchase Amount (USD)"].sum().sort_values(ascending = False)

itens_valor

# %%

cat = base.groupby("Category")["Purchase Amount (USD)"].sum().sort_values(ascending = False)

cat

# %%

idades = base.groupby(["Customer ID", "Age"])["Item Purchased"]


idades

# %%

base.head()