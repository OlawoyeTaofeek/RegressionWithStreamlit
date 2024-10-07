import streamlit as st 
import pandas as pd
import pickle

df_clean = pd.read_csv("cleaned_df.csv")
df_clean.drop(columns=['Unnamed: 0'], inplace=True)
print(df_clean.head())

with open("encoded_ocean_proximity.pkl", "rb") as f:
    encoder = pickle.load(f) 
    
with open("scaler.pkl", "rb") as f:
    scaling = pickle.load(f) 
    
print(type(scaling))
    
with open("best_model_random_forest.pkl", "rb") as f:
    model = pickle.load(f)
print(type(model))

df = pd.read_csv('housing.csv')

def pred_page():
    with st.expander("My DataFrame"):
        st.dataframe(df_clean)
        
    with st.sidebar:
        st.subheader("Input Features")
        
        longitude = st.slider('Longitude', min_value=df['longitude'].min(), max_value=df['longitude'].max(), value=df['longitude'].min())
        latitude = st.slider('Latitude', min_value=df['latitude'].min(), max_value=df['latitude'].max(), value=df['latitude'].min()) 
        housing_median_age = st.slider('Housing Median Age', min_value=0.0, max_value=100.0, value=20.0)
        median_income = st.slider('Median Income', df['median_income'].min(), df['median_income'].max(), df['median_income'].mean())
        ocean_proximity = st.radio("Ocean Proximity", options=df['ocean_proximity'].unique())
        households = st.slider("Household", df['households'].min(), df['households'].max(), df['households'].mean())
        total_rooms = st.slider('Total Rooms', df['total_rooms'].min(), df['total_rooms'].max(), df['total_rooms'].mean())
        total_bedrooms = st.slider('Total Bedrooms', df['total_bedrooms'].min(), df['total_bedrooms'].max(), df['total_bedrooms'].mean())
        population = st.slider("Population", df['population'].min(), df['population'].max(), df['population'].mean())
        
        input_data = pd.DataFrame({
            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [housing_median_age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [ median_income],
            'ocean_proximity': [ocean_proximity]  # Original ocean_proximity input
        })
        
    st.markdown("---")
    with st.expander("User Input conversion into Dataframe"):
        st.dataframe(input_data)
        
    encoded_value = encoder.transform(input_data[['ocean_proximity']]).toarray()
    df_cat = pd.DataFrame(encoded_value, columns=encoder.get_feature_names_out(['ocean_proximity']))
    input_df = pd.concat([input_data, df_cat], axis=1)
    input_df.drop(columns=['ocean_proximity'], inplace=True)
       
    st.markdown("---")
    with st.expander("User Input after encoding"):
        st.write(input_df)
    
    
    st.markdown("---")
    scale_input = scaling.transform(input_df)
    st.write(scale_input)
    st.title("Now Let's help you predict")
    
    prediction = model.predict(scale_input)
    
    def load_prediction(predictions):
        return f"""<h3 style='color:green;'>The prediction based on your input is: {predictions[0]}</h3>"""
    
    st.markdown(load_prediction(prediction), unsafe_allow_html=True)
    

