import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Global COVID-19 Dashboard",
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

# Sidebar filters
st.sidebar.title("Filter Options")
country = st.sidebar.selectbox("Select Country", options=df['Country'].unique())
metric = st.sidebar.radio("Select Metric", options=['Confirmed', 'Recovered', 'Deaths'])

# Filter and plot
filtered_df = df[df['Country'] == country]
fig = px.line(filtered_df, x='Date', y=metric, title=f"{metric} Cases Over Time in {country}")
st.plotly_chart(fig, use_container_width=True)

# Raw data toggle
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

st.markdown("---")
st.subheader("Additional Visualization")
st.write("Here you could add a global map, a heatmap, or comparison between countries using the same dataset.")
