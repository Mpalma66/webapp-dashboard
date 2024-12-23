import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el nuevo archivo CSV
data_path = 'vehicles_us.csv'
car_data = pd.read_csv(data_path)

st.header('Panel de Control de Consumo de Combustible')

hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Histograma del Consumo Combinado (mpg)')
    fig = px.histogram(car_data, x='comb08')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir Gráfico de Dispersión')
if scatter_button:
    st.write('Relación entre Consumo en Ciudad y Carretera')
    fig = px.scatter(car_data, x='city08', y='highway08')
    st.plotly_chart(fig, use_container_width=True)
