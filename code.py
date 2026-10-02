#configs iniciais
import streamlit as st
import pandas as pd
import plotly.express as px

#carregar base de dados
sales_table = pd.read_csv("vendas.csv")

#titulo
st.write("# Sistema de Vendas")

#cadastro vendas

st.sidebar.write("## Cadastrar Vendas")
    #data
date = st.sidebar.date_input("Data")
    #vendedor (ana, bruno e carla)
salesperson = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
    #produto (notebook, fone e celular)
product = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
    #quantidade
quantity = st.sidebar.number_input("Quantidade", step=1)
    #valor
value = st.sidebar.number_input("Valor")
    #botao cadastrar
cad_button = st.sidebar.button("Cadastrar venda")
        #adicionar venda na tabela
if cad_button:
    new_sale = [str(date), salesperson, product,quantity, value]
    last_sale = len(sales_table)
    sales_table.loc[last_sale] = new_sale
    sales_table.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada!")
#vendas cadastradas
st.write("## Vendas Cadastradas")

    #tabela de vendas
st.dataframe(sales_table)

#dashboard
st.write("## Dashboard")

    #faturamento
revenue = sales_table["valor"].sum()
st.metric("Faturamento Total", f"R$ {revenue}")

    #venda por vendedor (barra)
graphic1 = px.bar(sales_table, x="vendedor", y="valor", color="produto")
st.plotly_chart(graphic1)

    #vendas por produto (pizza)
graphic2 = px.pie(sales_table, names="produto", values="valor")
st.plotly_chart(graphic2)