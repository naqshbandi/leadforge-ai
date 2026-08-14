import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="LEADFORGE AI | Brand Up Digital", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# --- SESSION STATE ---
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'selected_plan' not in st.session_state: st.session_state.selected_plan = None
if 'page' not in st.session_state: st.session_state.page = 'Home'

# --- CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body {font-family: 'Poppins', sans-serif; background-color: #004D40;}
    .main {background-color: #004D40; color: #FFFFFF;}
    header {visibility: hidden;}
    .navbar {display: flex; justify-content: space-between; align-items: center; padding: 15px 5%; background-color: #00332E; border-bottom: 2px solid #90EE90;}
    .navbar-brand {color: #90EE90; font-size: 24px; font-weight: 700;}
    .navbar-brand span {color: #FFFFFF; font-size: 14px; font-weight: 400; display: block;}
    .card {background-color: #00695C; padding: 30px; border-radius: 15px; border: 1px solid #90EE90; margin: 20px 5%;}
    .pricing-card {background-color: #00695C; padding: 25px; border-radius: 15px; border: 2px solid #90EE90; text-align: center;}
    div[data-testid="stTextInput"]>div>div>input {background-color: #90EE90; color: #00332E; border-radius: 10px; border: 2px solid #FFFFFF; font-weight: 600;}
    .stButton>button {background: linear-gradient(90deg, #90EE90 0%, #32CD32 100%); color: #00332E; font-weight: 700; border-radius: 12px; height: 3.2em; border: none; width: 100%;}
    div[data-testid="stDataFrame"] {border: 2px solid #90EE90; border-radius: 12px; background-color: #00695C;}
    div[data-testid="stDataFrame"] * {color: #FFFFFF !important;}
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">🚀 LEADFORGE AI <span>By Brand Up Digital - World's #1 Lead Generation Agency</span></div>
</div>
""", unsafe_allow_html=True)

# --- PAGE LOGIC WITH LOCK ---
if st.session_state.page == 'Home':
    st.markdown('<h1 style="color:#90EE90; text-align:center;">Worlds #1 Free Lead Generation Tool</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up", use_container_width=True): st.session_state.page = 'Signup'
    with col2:
        if st.button("Login", use_container_width=True): st.session_state.page = 'Login'

elif st.session_state.page == 'Signup':
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Create Your Free Account")
        st.text_input("Email Address")
        st.text_input("Password", type="password")
        if st.button("Create Account"):
            st.session_state.logged_in = True
            st.session_state.page = 'Pricing' # SIGNUP KE BAAD DIRECT PRICING PE BHEJ DO
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'Login':
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Login to Your Account")
        st.text_input("Email Address")
        st.text_input("Password", type="password")
        if st.button("Sign In"):
            st.session_state.logged_in = True
            st.session_state.page = 'Pricing' # LOGIN KE BAAD BHI PRICING PE BHEJ DO
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'Pricing':
    if not st.session_state.logged_in:
        st.warning("Please Login First")
        st.session_state.page = 'Login'
        st.rerun()
        
    st.markdown("### Choose Your Plan to Unlock Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="pricing-card"><h3>Free Plan</h3><h2>$0</h2><p>100 Leads / Month</p></div>', unsafe_allow_html=True)
        if st.button("Select Free"): 
            st.session_state.selected_plan = "Free"
            st.session_state.page = 'Dashboard'
            st.rerun()
    with col2:
        st.markdown('<div class="pricing-card" style="border-color: #FFD700;"><h3>Pro Plan</h3><h2>$29</h2><p>5000 Leads / Month</p></div>', unsafe_allow_html=True)
        if st.button("Select Pro"): 
            st.session_state.selected_plan = "Pro"
            st.session_state.page = 'Dashboard'
            st.rerun()
    with col3:
        st.markdown('<div class="pricing-card"><h3>Agency Plan</h3><h2>$99</h2><p>Unlimited Leads</p></div>', unsafe_allow_html=True)
        if st.button("Select Agency"): 
            st.session_state.selected_plan = "Agency"
            st.session_state.page = 'Dashboard'
            st.rerun()

elif st.session_state.page == 'Dashboard':
    if not st.session_state.logged_in or st.session_state.selected_plan is None:
        st.error("Access Denied! Please Select a Plan First")
        st.session_state.page = 'Pricing'
        st.rerun()
    
    st.success(f"Welcome! You are on {st.session_state.selected_plan} Plan")
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Generate Your Leads")
        col1, col2, col3, col4 = st.columns(4)
        with col1: country = st.selectbox("Select Country", ["USA", "UK", "Canada", "Australia", "Pakistan", "UAE"])
        with col2: city = st.text_input("Enter City", "New York")
        with col3: industry = st.text_input("Enter Industry", "Doctors")
        
        max_leads = 100 if st.session_state.selected_plan == "Free" else 5000 if st.session_state.selected_plan == "Pro" else 500
        with col4: num_leads = st.slider("Number of Leads", 10, max_leads, 100)

        if st.button("Generate Leads", use_container_width=True):
            with st.spinner("Scraping Data..."): time.sleep(3)
            st.success(f"Found {num_leads} leads for {industry} in {city}, {country}")
            data = [{"Sr": i, "Business Name": f"{industry} {i}", "Phone": f"+1 {random.randint(100,999)} {random.randint(1000,9999)}", "Email": f"info{i}@test.com"} for i in range(1, num_leads + 1)]
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True, height=400)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, 'leads.csv', 'text/csv', use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
