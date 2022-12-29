import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from data_handling_service import rsi, sma


def st_plotter(datain):  # funcion para hacer los plots y su despliegue en streamlit
    datain = sma(datain)  # aplico la funcion "sma" para obtener la columna SMA
    datain = rsi(datain)  # aplico la funcion "rsi" para obtener la columna RSI

    st.header(f"Gráficos")

    f = go.Figure(data=[go.Candlestick(x=datain.index, open=datain['open'], high=datain['high'], low=datain['low'],
                                        close=datain['close'], name='Open, close, high y low'),
                        go.Scatter(x=datain.index, y=datain['20 SMA'], line=dict(color='purple', width=1),
                                   name='Media móvil')])
    f.update_layout(title='Media móvil y datos de open, close, low y high por día',
                    xaxis_title='Tiempo (días)',
                    yaxis_title='Media móvil')

    r = px.line(datain, x=datain.index, y='rsi')
    r.update_layout(title='RSI',
                    xaxis_title='Tiempo (días)',
                    yaxis_title='RSI')

    st.plotly_chart(f)
    st.plotly_chart(r)

