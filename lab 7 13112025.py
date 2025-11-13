import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium.plugins import HeatMap
import plotly.express as px

st.set_page_config(
    page_title="Global COVID-19 Heatmap",
    page_icon="🦠",
    layout="wide"
)   

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"

    df = pd.read_csv(url)
    df['Date'] = pd.to_datetime(df['Date'])
    return df
df = load_data()
st.sidebar.header("Filter Options")
country=st.sidebar.selectbox("Select Country", df['Country'].unique())
metric=st.sidebar.radio("Select Metric", ('Confirmed', 'Recovered', 'Deaths'))
filtered_df = df[df['Country'] == country]
fig = px.line(filtered_df, x='Date', y=metric, title=f'COVID-19 {metric} Cases in {country}')
st.plotly_chart(fig, use_container_width=True)

# Raw data toggle
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

st.markdown("---")
st.subheader("Additional Visualization")
st.write("Here you could add a global map, a heatmap, or comparison between countries using the same dataset.")
