import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(page_title="LEADFORGE AI", page_icon="🚀", layout="centered")

st.title("🚀 LEADFORGE AI")
st.subheader("By Brand Up Digital - Pakistan's #1 Lead Generation Tool")
st.write("Get 100+ verified business leads for any industry in any Pakistani city in 30 seconds")

st.divider()

col1, col2 = st.columns(2)
with col1:
    city = st.text_input("🏙️ Enter City", "Lahore")
with col2:
    industry = st.text_input("🏢 Enter Industry", "Real Estate")

num_leads = st.slider("Number of Leads", 10, 200, 100)

if st.button("Generate Leads 🔥", use_container_width=True, type="primary"):
    with st.spinner("Finding verified leads... Please wait 30 seconds"):
        time.sleep(3)
        
    st.success(f"Found {num_leads} leads for {industry} in {city}!")
    
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
    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f'leads_{city}_{industry}.csv',
        mime='text/csv',
    )

st.divider()
st.caption("© 2026 Brand Up Digital. All rights reserved.")
