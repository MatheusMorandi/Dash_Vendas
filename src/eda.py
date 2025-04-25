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

clt_total = len(base["Customer ID"].unique())

clt_total

# %%

base["Purchase Amount (USD)"] = base["Purchase Amount (USD)"].astype(float)

# %%

vnd_totais = round((base["Purchase Amount (USD)"].sum()), 2)

vnd_formatado = f"{vnd_totais:,.2f}"

# %%

tck_medio = round((vnd_totais/clt_total), 2)

tck_medio

# %%

avl_media = round(((base["Review Rating"].sum())/clt_total), 2)

avl_media

# %%

tx_assinatura = base["Subscription Status"].value_counts(normalize = True)

tx_assinatura = tx_assinatura.iloc[1] * 100

tx_assinatura = f"{tx_assinatura}%"

# %%

def grafico_idade(dados):

    grfc_idade = px.histogram(dados, 
                              dados["Age"], 
                              color = dados["Gender"], 
                              color_discrete_map = {"Male": "#2E91E5", "Female": "#E15F99"})

    grfc_idade.update_layout(
        title = "Distribuição de Idade",
        template = "plotly",
        margin = dict(l = 50, r = 50, b = 50, t = 50),
        xaxis_title = "",
        yaxis_title = "Quantidade de Clientes"
    )

    return grfc_idade


# %%

def grafico_generos(dados):

    generos = pd.Series(dados["Gender"].value_counts())

    grfc_gen = px.pie(data_frame = generos, 
                      names = generos.index, 
                      values = generos.values, 
                      color = generos.index, 
                      title = "Distribuição dos Gêneros", 
                      color_discrete_map = {"Male": "#2E91E5", "Female": "#E15F99"})

    return grfc_gen

# %%

def grafico_media_genero(dados):

    media_geral = dados["Purchase Amount (USD)"].mean()

    media_genero = dados.groupby("Gender", as_index = False)["Purchase Amount (USD)"].mean().round(2)

    grfc_gen_media = px.bar(data_frame = media_genero, 
                            x = media_genero["Gender"], 
                            y = media_genero["Purchase Amount (USD)"], 
                            color = media_genero["Gender"], 
                            color_discrete_map = {"Male": "#2E91E5", "Female": "#E15F99"})

    grfc_gen_media.update_layout(
        title = "Média de Gasto por Gênero (USD)",
        template = "plotly",
        margin = dict(l = 50, r = 50, b = 50, t = 50),
        xaxis_title = "",
        yaxis_title = "",
        showlegend = False
    )

    grfc_gen_media.add_hline(
        y = media_geral,
        line_dash = "dot",
        annotation_text = f"Média Geral: ${media_geral:.2f}",
        line_color = "red")

    return grfc_gen_media

# %%

def grafico_top_estado(dados):

    top_estado = dados.groupby("Location", as_index = False)["Purchase Amount (USD)"].sum().sort_values(by = "Purchase Amount (USD)", ascending = False).head(10)

    grfc_top_estado = px.bar(top_estado, 
                            x = top_estado["Purchase Amount (USD)"], 
                            y = top_estado["Location"], 
                            color = top_estado["Location"],
                            color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_top_estado.update_layout(
        title = "Top 10 Estados por Volume de Vendas (USD)",
        template = "plotly",
        margin = dict(l = 50, r = 50, b = 50, t = 50),
        xaxis_title = "",
        yaxis_title = "",
        showlegend = False)

    return grfc_top_estado

# %%

def grafico_categorias(dados):

    grfc_categorias = px.sunburst(
        data_frame = dados,
        path = ["Category", "Item Purchased"],
        values = "Purchase Amount (USD)",
        color = "Category",
        color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_categorias.update_layout(
            title = "Performance dos Produtos por Categoria, Item",
            template = "plotly",
            margin = dict(l = 50, r = 50, b = 50, t = 50))


    return grfc_categorias

# %%

def grafico_estacoes(dados):

    estacoes = dados.groupby(["Category", "Season"])["Purchase Amount (USD)"].sum().reset_index()

    grfc_estacao = px.imshow(
        estacoes.pivot(index = "Category", columns = "Season", values = "Purchase Amount (USD)"),
        labels = dict(x = "", y = "", color = "Valor Total (USD)"),
        title = "Valor Total de Compras por Categoria e Estação",
        color_continuous_scale = "Sunsetdark",
        text_auto = True)

    grfc_estacao.update_layout(
        xaxis = dict(side = "top"))

    return grfc_estacao

# %%

def grafico_itens(dados):

    itens = dados.groupby("Item Purchased", as_index = False)["Purchase Amount (USD)"].sum().sort_values(by = "Purchase Amount (USD)",ascending = False).head(10)

    grfc_itens = px.bar(
        itens,
        x = "Purchase Amount (USD)",
        y = "Item Purchased",
        color = "Item Purchased",
        color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_itens.update_layout(
        title = "Top 10 Itens por Volume de Vendas (USD)",
        template = "plotly",
        margin = dict(l = 50, r = 50, b = 50, t = 50),
        xaxis_title = "",
        yaxis_title = "",
        showlegend = False)

    return grfc_itens

# %%

def grafico_pagamentos(dados):

    pagamentos = dados["Payment Method"].value_counts().reset_index()

    pagamentos.columns = ["Método", "Contagem"]

    grfc_pagamento = px.pie(
        pagamentos,
        names = "Método",
        values = "Contagem",
        hole = 0.45,
        title = "Distribuição de Métodos de Pagamento",
        color = "Método",
        color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_pagamento.update_traces(
        textinfo = "percent+label",
        hovertemplate = "<b>%{label}</b><br>Quantidade de Compras: %{value}<br>Percentual: %{percent}")

    return grfc_pagamento

# %%

def grafico_media_pag(dados):

    media_pag = round((dados.groupby("Payment Method", as_index = False)["Purchase Amount (USD)"].mean().sort_values(by = "Purchase Amount (USD)", ascending = False)), 2)

    grfc_media_pag = px.bar(
        media_pag,
        x = "Purchase Amount (USD)",
        y = "Payment Method",
        color = "Payment Method",
        color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_media_pag.update_layout(
        title = "Valor Médio Gasto por Método de Pagamento",
        template = "plotly",
        margin = dict(l = 50, r = 50, b = 50, t = 50),
        xaxis_title = "",
        yaxis_title = "",
        showlegend = False)

    return grfc_media_pag

# %%

def grafico_fretes(dados):

    fretes = dados.groupby("Shipping Type", as_index = False)["Purchase Amount (USD)"].sum()

    grfc_fretes = px.pie(
        fretes,
        names = "Shipping Type",
        values = "Purchase Amount (USD)",
        color = "Shipping Type",
        hole = 0.45,
        title = "Proporção de tipos de frete utilizados",
        color_discrete_sequence = px.colors.qualitative.Pastel)

    grfc_fretes.update_traces(
        textinfo = "percent",
        hovertemplate = "<b>%{label}</b><br>Quantidade de Compras: %{value}<br>Percentual: %{percent}")


    return grfc_fretes

# %%

def grafico_desconto(dados):

    desconto = dados.groupby(["Category", "Discount Applied"], as_index = False)["Purchase Amount (USD)"].sum()

    grfc_desconto = px.bar(
        desconto,
        x = "Category",                   
        y = "Purchase Amount (USD)",     
        color = "Discount Applied",        
        barmode = "group",               
        title = "Vendas com vs. sem Desconto por Categoria",
        labels = {"Purchase Amount (USD)": "Total de Vendas (USD)"},
        color_discrete_sequence = px.colors.qualitative.Pastel, 
        text_auto = False)

    grfc_desconto.update_layout(
        xaxis_title = "Categoria",
        yaxis_title = "Total de Vendas (USD)",
        hovermode = "x unified")

    return grfc_desconto

# %%
