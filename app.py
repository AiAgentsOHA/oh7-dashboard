import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
st.set_page_config(page_title="OH7 Dashboard",page_icon="🌊",layout="wide",initial_sidebar_state="collapsed")
st.markdown("<style>#MainMenu,footer,.stApp>header{visibility:hidden}.block-container{padding:0}iframe{border:none!important}</style>",unsafe_allow_html=True)
html_file=Path(__file__).parent/"oh7_executive_dashboard_v9.html"
if html_file.exists():components.html(html_file.read_text(encoding='utf-8'),height=950,scrolling=True)
else:st.error("Dashboard not found")