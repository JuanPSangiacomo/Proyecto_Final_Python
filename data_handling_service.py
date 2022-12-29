def rsi(data, period=14):  # funcion que calcula el RSI
    try:
        data['gain'] = (data['close'] - data['open']).apply(lambda x: x if x > 0 else 0)
        data['loss'] = (data['close'] - data['open']).apply(lambda x: -x if x < 0 else 0)

        data['ema_gain'] = data['gain'].ewm(span=period, min_periods=period).mean()
        data['ema_loss'] = data['loss'].ewm(span=period, min_periods=period).mean()

        data['rs'] = data['ema_gain'] / data['ema_loss']

        data['rsi'] = 100 - (100 / (data['rs'] + 1))

        return data

    except ValueError:
        print('Asegúrese de que el dataframe utilizado tenga la columnas utilizadas por la función')


def sma(data):  # funcion que calcula la media movil
    try:
        data['20 SMA'] = data['close'].rolling(20).mean()

        return data

    except ValueError:
        print("Asegúrese de que el dataframe utilizado tenga la columna 'Close'")
