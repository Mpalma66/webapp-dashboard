import pandas as pd
import plotly.express as px
import streamlit as st
import requests

# URL del archivo CSV (Google Drive o Dropbox)
csv_url = 'https://drive.google.com/file/d/1ZRPsX_IogWxUSJnK6sYpdFkRCcp4kP8a/view?usp=sharingID'

@st.cache
def load_data(url):
    response = requests.get(url)
    with open('vehicles_us.csv', 'wb') as f:
        f.write(response.content)
    return pd.read_csv('vehicles_us.csv')

car_data = load_data(csv_url)

st.header('Panel de Control de Ventas de Vehículos')

hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir Gráfico de Dispersión')
if scatter_button:
    st.write('Gráfico de Dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
