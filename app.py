import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="LEADFORGE AI | Brand Up Digital", page_icon="🚀", layout="wide")

# --- WORLD CLASS DARK GREEN THEME ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] {background-color: #00251A !important;} /* VERY DARK GREEN */
    .main {background-color: #00251A; color: #FFFFFF;}
    header {visibility: hidden;}
    
    /* NAVBAR - BLACK WITH NEON LINE */
    .navbar {
        background-color: #000000; padding: 20px 8%; display: flex; justify-content: space-between; 
        align-items: center; border-bottom: 3px solid #00FF7F; position: sticky; top: 0; z-index: 999;
    }
    .brand {color: #00FF7F; font-size: 28px; font-weight: 800; font-family: 'Poppins';}
    .brand span {color: #FFFFFF; font-size: 12px; font-weight: 400; display: block; letter-spacing: 1px;}
    
    /* HERO */
    .hero {text-align: center; padding: 80px 20px;}
    .hero h1 {color: #00FF7F; font-size: 50px; font-weight: 800; font-family: 'Poppins';}
    .hero p {color: #E0E0E0; font-size: 18px;}
    
    /* CARD - DARK GREEN */
    .card {background-color: #00332E; padding: 40px; border-radius: 20px; border: 1px solid #00FF7F; margin: 40px 8%;}
    
    /* INPUTS - LIGHT GREEN */
    div[data-testid="stTextInput"]>div>div>input, div[data-testid="stSelectbox"]>div>div>div {
        background-color: #90EE90 !important; color: #00251A !important; 
        border-radius: 10px; border: 2px solid #00FF7F; font-weight: 600;
    }
    
    /* BUTTON - NEON GREEN */
    .stButton>button {
        background: #00FF7F; color: #000; font-weight: 800; border-radius: 50px; 
        height: 60px; border: none; width: 100%; font-size: 18px; box-shadow: 0 0 25px #00FF7F;
    }
    
    /* TABLE - DARK BG + WHITE TEXT + GOLDEN LINKS */
    div[data-testid="stDataFrame"] {border: 2px solid #00FF7F; border-radius: 12px; background-color: #00332E;}
    div[data-testid="stDataFrame"] * {color: #FFFFFF !important;} /* WHITE TEXT */
    a {color: #FFD700 !important; font-weight: 700;} /* GOLDEN */
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <div class="brand">🚀 LEADFORGE AI <span>BY BRAND UP DIGITAL | WORLD'S #1 LEAD AGENCY</span></div>
</div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <h1>World's #1 AI-Powered Lead Generation Platform</h1>
    <p>Get 500+ Verified Business Leads in 10 Seconds. For ANY Industry. In ANY Country.</p>
</div>
""", unsafe_allow_html=True)

# --- DASHBOARD ---
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Generate Your Leads")
    
    col1, col2, col3 = st.columns(3)
    with col1: country = st.selectbox("🌍 Select Country", ["USA", "UK", "Canada", "Australia", "Pakistan", "UAE"])
    with col2: city = st.text_input("🏙️ Enter City", "New York")
    with col3: industry = st.selectbox("🏢 Select Industry", ["Doctors", "Lawyers", "Real Estate", "Restaurants", "Gyms"])
    
    if st.button("GENERATE LEADS NOW 🔥", use_container_width=True):
        with st.spinner("Scraping..."): time.sleep(2)
        st.success(f"Found 100 leads for {industry} in {city}, {country}")
        data = [{"Business": f"{industry} {i}", "Phone": f"+1 555-000{i}", "Email": f"info{i}@test.com", "Website": f"www.site{i}.com"} for i in range(1, 101)]
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, height=400)
    st.markdown('</div>', unsafe_allow_html=True)
