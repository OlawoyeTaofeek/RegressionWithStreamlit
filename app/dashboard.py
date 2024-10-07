import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned DataFrame
df = pd.read_csv("housing.csv")

def dashboard_page():
    st.title("Feature Insights Dashboard")

    st.markdown("""<h2 style="color:green;">
    This dashboard provides insights into various features of the dataset. You can explore the relationships and distributions of these features.
    </h2>""", unsafe_allow_html=True)

    # Sidebar for filter selectors
    with st.sidebar:
        st.header("Filter Options")

        # Ocean Proximity Filter
        ocean_proximity_filter = st.multiselect(
            'Select Ocean Proximity Types',
            options=df['ocean_proximity'].unique(),
            default=df['ocean_proximity'].unique()
        )

        # Housing Median Age slider
        housing_median_age_range = st.slider('Filter by Housing Median Age', 
                                             min_value=int(df['housing_median_age'].min()), 
                                             max_value=int(df['housing_median_age'].max()), 
                                             value=(int(df['housing_median_age'].min()), int(df['housing_median_age'].max())))

    # Filter data based on sidebar selections
    filtered_df = df[df['ocean_proximity'].isin(ocean_proximity_filter)]
    filtered_df = filtered_df[(filtered_df['housing_median_age'] >= housing_median_age_range[0]) & 
                              (filtered_df['housing_median_age'] <= housing_median_age_range[1])]

    # Plot layout with multiple columns
    col1, col2 = st.columns(2)

    # Feature 1: Distribution of Longitude and Latitude
    with col1:
        st.subheader("Distribution of Longitude and Latitude")
        fig1 = px.scatter(filtered_df, x='longitude', y='latitude', 
                          color='ocean_proximity', 
                          title="Longitude vs Latitude with Ocean Proximity",
                          labels={'longitude': 'Longitude', 'latitude': 'Latitude'})
        st.plotly_chart(fig1, use_container_width=True)

    # Feature 2: Housing Median Age Distribution
    with col2:
        st.subheader("Housing Median Age Distribution")
        fig2 = px.histogram(filtered_df, x='housing_median_age', nbins=50, 
                            title="Distribution of Housing Median Age", 
                            labels={'housing_median_age': 'Housing Median Age'})
        st.plotly_chart(fig2, use_container_width=True)

    # Feature 3: Total Rooms vs Total Bedrooms
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Total Rooms vs Total Bedrooms")
        fig3 = px.scatter(filtered_df, x='total_rooms', y='total_bedrooms', 
                          title="Total Rooms vs Total Bedrooms",
                          labels={'total_rooms': 'Total Rooms', 'total_bedrooms': 'Total Bedrooms'})
        st.plotly_chart(fig3, use_container_width=True)

    # Feature 4: Population vs Households
    with col4:
        st.subheader("Population vs Households")
        fig4 = px.scatter(filtered_df, x='population', y='households', 
                          title="Population vs Households",
                          labels={'population': 'Population', 'households': 'Households'})
        st.plotly_chart(fig4, use_container_width=True)

    # Feature 5: Median House Value Distribution
    st.subheader("Median House Value Distribution")
    fig5 = px.histogram(filtered_df, x='median_house_value', nbins=50, 
                        title="Distribution of Median House Value", 
                        labels={'median_house_value': 'Median House Value'})
    st.plotly_chart(fig5, use_container_width=True)

    # Feature 6: Boxplot of Ocean Proximity and House Value
    st.subheader("House Value Distribution by Ocean Proximity")
    fig6 = px.box(filtered_df, x='ocean_proximity', y='median_house_value', 
                  title="House Value Distribution by Ocean Proximity", 
                  labels={'ocean_proximity': 'Ocean Proximity', 'median_house_value': 'House Value'})
    st.plotly_chart(fig6, use_container_width=True)

    # Summary statistics as a table
    st.subheader("Summary Statistics")
    st.write(filtered_df.describe())

