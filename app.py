import streamlit as st

from streamlit_option_menu import option_menu

from paginas.sobre import sobre

from paginas.dashboard import dashboard

from paginas.contato import contato



st.set_page_config(
    page_title="Dash de Vendas", 
    layout="wide",
    page_icon="🛒"
)

st.markdown("""
    <style>
        /* Reduz tamanho dos títulos */
        h1 {
            font-size: 32px !important;
            padding-bottom: 0.5rem !important;
            margin: 0.5rem 0 !important;
        }
        
        /* Ajusta subtítulos */
        h2 {
            font-size: 24px !important;
            margin: 0.3rem 0 !important;
        }
        
        /* Texto normal */
        p, li {
            font-size: 16px !important;
        }
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

if selected == "Sobre":

    sobre()

elif selected == "Dashboard":

    dashboard()

elif selected == "Contato":

    contato()
