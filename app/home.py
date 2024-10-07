import streamlit as st

def home_page():
    st.title("Welcome to the House Price Prediction App")
    
    # Display a relevant image about house price prediction
    st.image("house image.jpg", caption="House Price Prediction", use_column_width=True)

    st.markdown("""
    <h3 style="color:blue;">
    Predicting house prices can be a challenging task, but with the power of machine learning, we make it simple and efficient! 
    This app is designed to help users estimate house prices based on a variety of features like location, age, rooms, and more.
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### How it works:
    1. Input the features of the house such as **longitude**, **latitude**, **total rooms**, **households**, and **ocean proximity**.
    2. Our machine learning model, trained on historical data, will predict the **median house value** for your inputs.
    3. Explore feature insights and visualize data trends using our **interactive dashboard**.

    This project is powered by **Random Forest Regressor**, which gives us great accuracy for predictions.
    """)

    st.markdown("""
    ---
    ### About this Project:
    """)
    st.info("""
         This project uses a dataset that contains house pricing data from California, including features like location, number of rooms, 
         and proximity to the ocean. With this app, you can explore how different features influence house prices and make your own predictions!
      """)
