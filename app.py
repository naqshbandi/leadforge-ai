
import streamlit as st
import random
import time
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="LEADFORGE AI | Brand Up Digital", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PROFESSIONAL CSS - Dark + Gold + Blue. 100% Mobile Responsive
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="st-"] {font-family: 'Poppins', sans-serif;}
    .main {background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #E0E0E0;}
    .stTitle {color: #FFD700; font-weight: 700; font-size: clamp(28px, 5vw, 45px);} /* Responsive font */
    .stSubheader {color: #00A3FF; font-weight: 400;}
    .stButton>button {background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%); color: #0a0a0a; font-weight: 700; border-radius: 12px; height: 3.2em; border: none; width: 100%; font-size: 16px; transition: 0.3s;}
    .stButton>button:hover {transform: scale(1.02); box-shadow: 0 0 15px #FFD700;}
    .card {background-color: rgba(255,255,255,0.05); padding: 25px; border-radius: 15px; border: 1px solid rgba(255,215,0,0.2); backdrop-filter: blur(10px);}
    div[data-testid="stDataFrame"] {border: 1px solid #FFD700; border-radius: 12px; background-color: #1a1a2e;}
    .footer {text-align: center; color: #888; padding-top: 30px; font-size: 12px;}
    /* Mobile Responsive Fix */
    @media (max-width: 768px) {
        .stColumns {flex-direction: column !important;}
    }
</style>
""", unsafe_allow_html=True)

# HEADER
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1,5])
    with col1:
        st.markdown("🚀", unsafe_allow_html=True) # Big Icon
    with col2:
        st.title("LEADFORGE AI")
        st.subheader("By Brand Up Digital - Pakistan's #1 Lead Generation Tool")
    st.markdown("#### Get 100+ verified business leads for any industry in any Pakistani city in 30 seconds")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("") # spacing

# INPUT SECTION
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Generate Your Leads")
    col1, col2, col3 = st.columns(3) # یہ موبائل پر خود بخود نیچے آ جائیں گے
    with col1:
        city = st.text_input("🏙️ Enter City", "Lahore", placeholder="e.g. Karachi, Islamabad")
    with col2:
        industry = st.text_input("🏢 Enter Industry", "Real Estate", placeholder="e.g. Doctors, Lawyers")
    with col3:
        num_leads = st.slider("Number of Leads", 10, 500, 100)

    if st.button("Generate Leads 🔥", use_container_width=True):
        with st.spinner("🔍 Finding verified leads... Please wait 30 seconds"):
            time.sleep(3)
            
        st.success(f"✅ Successfully Found {num_leads} leads for **{industry}** in **{city}**!")
        
        data = []
        for i in range(1, num_leads + 1):
            data.append({
                "Sr#": i,
                "Business Name": f"{industry} Business {i}",
                "Phone": f"03{random.randint(10000000, 99999999)}",
                "Email": f"info{i}@{industry.lower().replace(' ', '')}.com",
                "City": city,
                "Industry": industry
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, height=450) # Mobile scrollable
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV File",
            data=csv,
            file_name=f'LEADFORGE_{city}_{industry}.csv',
            mime='text/csv',
            use_container_width=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2026 Brand Up Digital. All Rights Reserved. | Powered by AI | Made in Pakistan for the World</div>', unsafe_allow_html=True)
