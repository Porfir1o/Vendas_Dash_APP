import streamlit as st
from dash import Dash
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_map_mensal, grafico_rec_estado,grafico_rec_categoria,grafico_rec_vendedores,grafico_vendas_vendedores

# formato da pagina
st.set_page_config(page_title="Vendas", layout='wide')

# titulo
st.title("Dashboard de Vendas :shopping_trolley:")

# Filtros Dashboard

st.sidebar.title('Filtros')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    sorted(
            df['Vendedor'].unique()
    )
)
filtro_categoria = st.sidebar.multiselect(
    'Categoria de Produto',
    sorted(
            df['Categoria do Produto'].str.capitalize().unique()
    )
)
filtro_loc_compra = st.sidebar.multiselect(
    'Local da Compra',
    sorted(
            df['Local da compra'].unique()
    )
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

if filtro_categoria:
    df = df[df['Categoria do Produto'].isin(filtro_categoria)]

if filtro_loc_compra:
    df = df[df['Local da compra'].isin(filtro_loc_compra)]

aba1, aba2, aba3 = st.tabs(['Dados Análiticos', 'Gráficos', 'Análise por Vendedor'])

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
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

