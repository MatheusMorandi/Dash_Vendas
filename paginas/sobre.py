import streamlit as st

def sobre():

    st.markdown("""
    <style>
        .main-title {
            color: #E2E8F0 !important;
            text-align: center !important;
            margin-bottom: 2 rem !important;
            padding: 1rem !important;
        }
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] {
            background: #1A1D23 !important;
            padding: 1.5rem !important;
            border-radius: 12px !important;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3) !important;
            margin: 1.5rem 0 !important;
            border-left: 4px solid #2D3748 !important;
        }
        .methodology-step {
            padding: 0.8rem !important;
            background: #252935 !important;
            border-radius: 8px !important;
            margin: 0.5rem 0 !important;
            color: #E2E8F0 !important;
        }
        .tech-badge {
            padding: 0.5rem 1rem !important;
            background: #2D3748 !important;
            border-radius: 25px !important;
            border: 1px solid #4A5568 !important;
            display: inline-flex !important;
            align-items: center !important;
            margin: 0.2rem !important;
            transition: all 0.3s ease !important;
        }
        .tech-badge:hover {
            background: #3C4555 !important;
            transform: translateY(-2px) !important;
        }
        .tech-badge a {
            color: #63B3ED !important;
            text-decoration: none !important;
            align-items: center !important;
            gap: 1 rem !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #CBD5E0 !important;
        }
        .kaggle-img {
            filter: invert(0.8);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 class="main-title">
            📌 Sobre o Projeto
        </h1>
    """, unsafe_allow_html=True)

    with st.container():

        st.subheader("🎯 Objetivo Principal")

        st.markdown("""
            <div class="methodology-step">📈 Análise de tendências de vendas históricas</div>
            <div class="methodology-step">🔄 Identificação de padrões sazonais</div>
        """, unsafe_allow_html=True)

    with st.container():
        
        col1, col2 = st.columns([1, 2], gap="medium")
        
        with col1:
            st.markdown("#### 📂 Fonte dos Dados")
            st.markdown("""
            <div class="tech-badge">
                <a href="https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset" target="_blank">
                    <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png" width="20">
                    Kaggle
                </a>
            </div>""", unsafe_allow_html=True)
            
        with col2:
            st.markdown("#### 🧪 Processo ETL")
            st.markdown("""
                <div class="methodology-step">1. Coleta dos Dados</div>
                <div class="methodology-step">2. Limpeza e Validação</div>
                <div class="methodology-step">3. Transformação e Enriquecimento</div>
                <div class="methodology-step">4. Análise Estatística</div>
                <div class="methodology-step">5. Visualização Interativa</div>
            """, unsafe_allow_html=True)

    
    with st.container():

        st.subheader("🛠️ Stacks ")

        st.markdown("""
            <div class="tech-badge">
                <a href="https://python.org" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="20">
                    Python
                </a>
            </div>
            <div class="tech-badge">
                <a href="https://pandas.pydata.org" target="_blank">
                    <img src="https://pandas.pydata.org/static/img/pandas_secondary.svg" width="20">
                    Pandas
                </a>
            </div>
            <div class="tech-badge">
                <a href="https://streamlit.io" target="_blank">
                    <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="20">
                    Streamlit
                </a>
            </div>
            <div class="tech-badge">
                <a href="https://plotly.com" target="_blank">
                    <img src="https://images.plot.ly/logo/new-branding/plotly-logomark.png" width="20">
                    Plotly
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    with st.container():

        st.subheader("📚 Dicionário dos Dados ")

        st.markdown("""
            <div class="methodology-step">🆔 Customer ID - Identificador único para cada cliente.</div>
            <div class="methodology-step">🎂 Age - Idade do cliente.</div>
            <div class="methodology-step">🚻 Gender - Gênero do cliente (Masculino/Feminino).</div>
            <div class="methodology-step">🛒 Item Purchased - Item comprado pelo cliente.</div>
            <div class="methodology-step">📦 Category - Categoria do item comprado.</div>
            <div class="methodology-step">💵 Purchase Amount (USD) - Valor da compra em dólares.</div>
            <div class="methodology-step">📍 Location - Estado onde a compra foi realizada.</div>
            <div class="methodology-step">📏 Size - Tamanho do item comprado.</div>
            <div class="methodology-step">🎨 Color - Cor do item comprado.</div>
            <div class="methodology-step">🌞 Season - Estação do ano da compra.</div>
            <div class="methodology-step">⭐ Review Rating - Avaliação do cliente.</div>
            <div class="methodology-step">🔔 Subscription Status - Assinatura (Sim/Não).</div>
            <div class="methodology-step">🚚 Shipping Type - Tipo de envio escolhido.</div>
            <div class="methodology-step">💲 Discount Applied - Desconto aplicado (Sim/Não).</div>
            <div class="methodology-step">🎟️ Promo Code Used - Código promocional utilizado.</div>
            <div class="methodology-step">🛍️ Previous Purchases - Número de compras anteriores.</div>
            <div class="methodology-step">💳 Payment Method - Método de pagamento preferencial.</div>                            
            """, unsafe_allow_html=True)

    
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