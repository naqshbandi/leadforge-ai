import streamlit as st
import random
import time
import pandas as pd

# SESSION STATE FOR LOGIN
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

st.set_page_config(page_title="LEADFORGE AI | Brand Up Digital", page_icon="🚀", layout="wide")

# --- FINAL PROFESSIONAL CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body {font-family: 'Poppins', sans-serif; background-color: #001F3F;} /* NAVY BLUE */
    .main {background-color: #001F3F; color: #FFFFFF;}
    .stTitle {color: #00FF7F; font-weight: 700;} /* LIGHT GREEN */
    .stSubheader {color: #ADD8E6;} /* LIGHT BLUE */
    .card {background-color: #004D40; padding: 25px; border-radius: 15px; border: 1px solid #00FF7F; margin-bottom: 20px;} /* DARK GREEN */
    div[data-testid="stTextInput"]>div>div>input {background-color: #E0F7FA; color: #001F3F; border-radius: 10px; border: 2px solid #00FF7F; font-weight: 600;} /* LIGHT BLUE BOX */
    .stButton>button {background: linear-gradient(90deg, #00FF7F 0%, #32CD32 100%); color: #001F3F; font-weight: 700; border-radius: 12px; height: 3.2em; border: none; width: 100%;}
    .pricing-card {background-color: #004D40; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #00FF7F;}
</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
col1, col2, col3, col4 = st.columns([3,1,1,1])
with col1: st.title("🚀 LEADFORGE AI")
with col2: 
    if st.button("Home"): st.session_state.page = 'Home'
with col3: 
    if st.button("Pricing"): st.session_state.page = 'Pricing'
with col4: 
    if st.button("Login" if not st.session_state.logged_in else "Dashboard"): st.session_state.page = 'Login'

# --- PAGE LOGIC ---
if st.session_state.page == 'Home':
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### World's #1 Free Lead Generation Tool")
        st.markdown("Get 500+ verified business leads for ANY industry in ANY city WORLDWIDE")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'Pricing':
    st.markdown("### 💎 Choose Your Plan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="pricing-card"><h3>Free</h3><h2>$0</h2><p>100 Leads / Month</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="pricing-card" style="border-color: #FFD700;"><h3>Pro</h3><h2>$29</h2><p>5000 Leads / Month</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="pricing-card"><h3>Agency</h3><h2>$99</h2><p>Unlimited Leads</p></div>', unsafe_allow_html=True)

elif st.session_state.page == 'Login':
    if not st.session_state.logged_in:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Login / Sign Up")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Sign In"):
                st.session_state.logged_in = True
                st.success("Logged In Successfully!")
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.success("Welcome to your Dashboard!")
        # یہاں لیڈ جنریشن والا فارم آئے گا
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🎯 Generate Your Leads")
            city = st.text_input("🏙️ Enter City", "London")
            industry = st.text_input("🏢 Enter Industry", "Doctors")
            num_leads = st.slider("Number of Leads", 10, 500, 100)
            if st.button("Generate Leads 🔥"):
                with st.spinner("Scraping..."): time.sleep(2)
                st.dataframe(pd.DataFrame([{"Name":f"{industry} {i}", "Phone": f"+44 {random.randint(1000,9999)}"} for i in range(num_leads)]))
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:grey;'>© 2026 Brand Up Digital</p>", unsafe_allow_html=True)
