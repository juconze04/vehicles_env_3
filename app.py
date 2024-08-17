import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('C:\\Users\\Hewlett Packard\\projecto_vehicles_env_3\\vehicles_env_3-1\\vehicles_us.csv')

# Encabezado
st.header("Generador de Gráficos")

# Casillas de verificación para seleccionar los gráficos
hist_button = st.checkbox('Mostrar histograma')
disp_button = st.checkbox('Mostrar gráfico de dispersión')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_histogram = px.histogram(car_data, x="odometer", title='Histograma de Odometer')
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_histogram, use_container_width=True)


if disp_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title='Gráfico de Dispersión de Odometer vs Precio')
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)