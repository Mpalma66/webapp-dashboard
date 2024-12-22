import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el dataset actualizado
car_data = pd.read_csv('vehicles_us.csv')

st.header('Panel de Control de Ventas de Vehículos')

# Botón para histograma del odómetro
hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión (odómetro vs precio)
scatter_button = st.button('Construir Gráfico de Dispersión')
if scatter_button:
    st.write('Gráfico de Dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
