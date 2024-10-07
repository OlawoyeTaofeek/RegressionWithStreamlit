import streamlit as st          
from streamlit_option_menu import option_menu  
from home import home_page 
from predictions import pred_page
from dashboard import dashboard_page


# Page Configuration
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="PredictPrice"
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction", "Dashboard"], 
        icons=["house", "", ""], 
        menu_icon="cast",
    )
    
# Display home page if selected
if selected == "Home":
   home_page()

# Prediction Page with Sidebar Inputs
elif selected == "Prediction":
    pred_page()

elif selected == "Dashboard":
    dashboard_page()