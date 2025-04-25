import streamlit as st

def contato():

    st.markdown("""
    <style>
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] {
            background: #1A1D23 !important;
            padding: 1.5rem !important;
            border-radius: 12px !important;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3) !important;
            margin: 1.5rem 0 !important;
            border-left: 4px solid #2D3748 !important;
        }
        .profile-pic {
            width: 200px !important;
            height: 200px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 4px solid #63B3ED !important;
            margin: 0 auto 1.5rem !important;
            box-shadow: 0 4px 15px rgba(99, 179, 237, 0.2) !important;
        }
        .social-badges {
            display: flex !important;
            justify-content: center !important;
            gap: 1.5rem !important;
            margin-top: 2rem !important;
            flex-wrap: wrap !important;
        }
        .social-badges a {
            transition: all 0.3s ease !important;
        }
        .social-badges a:hover {
            transform: translateY(-3px) !important;
        }
        .bio-text {
            color: #CBD5E0 !important;
            line-height: 1.7 !important;
            font-size: 1.1rem !important;
        }
        h1, h2, h3 {
            color: #CBD5E0 !important;
        }
    </style>
    """, unsafe_allow_html=True)


    with st.container():
        
        st.markdown("""
            <h1 style='text-align: center; margin-bottom: 2.5rem;'>
                💻 Desenvolvido por Matheus Morandi
            </h1>
        """, unsafe_allow_html=True)

        
        col1, col2 = st.columns([1, 2], gap="medium")
        
        with col1:
            st.markdown("""
                <img src="https://avatars.githubusercontent.com/u/100449058?v=4" 
                     class="profile-pic" 
                     alt="Foto de Perfil">
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
                <h3 style='margin-bottom: 1rem;'>🦾 Sobre Mim</h3>
                <div class="bio-text">
                    <p>
                        Analista de Dados apaixonado por transformar números em insights!
                        Aqui você pode me encontrar nas redes:
                    </p>
                </div>
                
                <div class="social-badges">
                    <a href="https://www.linkedin.com/in/matheusmorandi/" target="_blank">
                        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="45">
                    </a>
                    <a href="https://github.com/MatheusMorandi" target="_blank">
                        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="45">
                    </a>
                </div>
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