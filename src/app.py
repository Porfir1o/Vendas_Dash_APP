import streamlit as st
from dash import Dash
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_map_mensal, grafico_rec_estado,grafico_rec_categoria,grafico_rec_vendedores,grafico_vendas_vendedores

#app = Dash(__name__)
#server = app.server

# formato da pagina
st.set_page_config(page_title="Vendas", layout='wide')

# titulo
st.title("Dashboard de Vendas :shopping_trolley:")

# Filtros Dashboard

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2, aba3 = st.tabs(['Base', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(),'R$'))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)

    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_map_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)

    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores, use_container_width=True)

