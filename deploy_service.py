import pandas as pd
import streamlit as st
from api_connect import cripto_download
from plotting_service import st_plotter


st.title("Entrega final python: Cotización cryptos y visualización")
st.markdown("En esta interfaz podrá graficar la cotización de diversas cryptomonedas. Para ello seleccione "
            "una moneda de la lista provista")
st.header("Información provista por KRAKEN")
st.markdown("Datos de open, close, low y high para la cryptomoneda seleccionada")

crypto_dropdown = st.selectbox(label='Seleccione una criptomoneda', options=('SOLUSD', 'BTCUSD', 'LUNAUSD', 'ETHUSD',
                                                                             'ADAUSD'))

df = cripto_download(crypto_dropdown)

st_plotter(df)
