import streamlit as st
from etapa1 import *

st.title("Monitor de Cotações de Moedas")
moedasDisponiveis = ["USD", "EUR", "BTC", "BRL", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY"]
origem = st.selectbox("Selecione a moeda de origem:", moedasDisponiveis, index=0)
destino = st.selectbox("Selecione a moeda de destino:", moedasDisponiveis, index=1)
valor = st.number_input("Insira o valor a ser convertido:", min_value=0.0, value=100.0)
column1, column2 = st.columns(2)
with column1:
    if st.button("Buscar Cotação"):
        cotacao = buscar_cotacao(origem, destino)
        st.success(f"Cotação Atual ({origem}/{destino}): {float(cotacao):.2f}")
with column2:
    if st.button("Realizar Conversão"):
        cotacao = float(rota_converter(valor, origem, destino))
        st.success(f"Valor Convertido: {float(cotacao):.2f}")
