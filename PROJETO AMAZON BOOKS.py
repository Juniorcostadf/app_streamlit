import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# Carregar os dados
df_reviews = pd.read_csv('/content/customer reviews.csv')
df_top100_books = pd.read_csv('/content/Top-100 Trending Books.csv')

# Definir os valores máximos e mínimos para preço e avaliação
price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()

rate_max = df_top100_books['rating'].max()
rate_min = df_top100_books['rating'].min()

# Slider para avaliação (rating)
max_rate = st.sidebar.slider('Rating Range', rate_min, rate_max, rate_max)

# Slider para preço (price)
max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)

# Filtro aplicando tanto o preço quanto a avaliação
df_books = df_top100_books[(df_top100_books['book price'] <= max_price) & (df_top100_books['rating'] <= max_rate)]

# Mostrar os livros filtrados
df_books

# Gráficos
fig = px.bar(df_books['year of publication'].value_counts(), title='Contagem por Ano de Publicação')
fig2 = px.histogram(df_books['book price'], title='Distribuição dos Preços dos Livros')

# Exibir os gráficos lado a lado
col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)

