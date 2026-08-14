# --- FINAL PRO CSS: DARK GREEN + LIGHT GREEN + GOLDEN LINKS + WHITE TEXT ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body {font-family: 'Poppins', sans-serif; background-color: #004D40;} /* DARK GREEN BACKGROUND */
    .main {background-color: #004D40; color: #FFFFFF;}
    .stApp {background-color: #004D40;}
    header {visibility: hidden;}
    
    /* NAVBAR */
    .navbar {display: flex; justify-content: space-between; align-items: center; padding: 15px 5%; background-color: #00332E; border-bottom: 2px solid #90EE90;}
    .navbar-brand {color: #90EE90; font-size: 24px; font-weight: 700;} /* LIGHT GREEN */
    .navbar-brand span {color: #FFFFFF; font-size: 14px; font-weight: 400; display: block;} /* WHITE */
    
    /* HERO + CARD */
    .hero h1 {color: #90EE90; font-size: clamp(28px, 5vw, 50px); font-weight: 700;} /* LIGHT GREEN HEADING */
    .hero p {color: #FFFFFF;} /* WHITE TEXT */
    .card {background-color: #00695C; padding: 30px; border-radius: 15px; border: 1px solid #90EE90; margin: 20px 5%;} /* DARK GREEN CARD */
    
    /* INPUTS - LIGHT GREEN BOX */
    div[data-testid="stTextInput"]>div>div>input, div[data-testid="stSelectbox"]>div>div>div {
        background-color: #90EE90; /* LIGHT GREEN */
        color: #00332E; /* DARK GREEN TEXT */
        border-radius: 10px; border: 2px solid #FFFFFF; font-weight: 600;
    }
    
    /* BUTTON - LIGHT GREEN */
    .stButton>button {
        background: linear-gradient(90deg, #90EE90 0%, #32CD32 100%); 
        color: #00332E; font-weight: 700; border-radius: 12px; height: 3.2em; border: none; width: 100%;
    }
    
   
