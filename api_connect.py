import krakenex
import pandas as pd
from pykrakenapi import KrakenAPI


def cripto_download(currency):  # funcion que conecta con la API REST de Kraken y baja un DataFrame
    try:
        api = krakenex.API()
        k = KrakenAPI(api)
        ohlc = k.get_ohlc_data(currency, interval=1440, ascending=True)

        return pd.DataFrame(ohlc[0])

    except ValueError:
        print('Chequee su conexion a internet')