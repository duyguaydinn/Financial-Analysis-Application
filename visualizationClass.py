import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

class DataVisualizer:
    def plot_price_series(self, data: pd.DataFrame, column: str, ticker: str):
        plt.plot(data.index, data[column])
        plt.title(f'Price Series of {ticker} ({column})')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

    def plot_moving_average(self, data: pd.DataFrame, column: str, window: int, ticker: str):
        data['Moving Average'] = data[column].rolling(window=window).mean()
        plt.plot(data.index, data[column], label=column)
        plt.plot(data.index, data['Moving Average'], label=f'{window}-Day Moving Average')
        plt.title(f'{window}-Day Moving Average of {ticker} ({column})')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def plot_volume(self, data: pd.DataFrame, ticker: str):
        plt.bar(data.index, data['Volume'])
        plt.title(f'Volume over Time for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.show()

    def plot_rsi(self, data: pd.DataFrame, ticker: str, column='Close', window=14):
        delta = data[column].diff(1)
        gain = delta.mask(delta < 0, 0)
        loss = -delta.mask(delta > 0, 0)
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        plt.plot(data.index, rsi)
        plt.axhline(30, linestyle='--', alpha=0.5, color='red')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.title(f'Relative Strength Index (RSI) for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.show()

    def plot_candlestick(self, data: pd.DataFrame, ticker: str):
        mpf.plot(data, type='candle', style='charles', volume=True, title=f'Candlestick Chart for {ticker}', show_nontrading=True)

    def plot_bollinger_bands(self, data: pd.DataFrame, column: str, ticker: str, window: int=20):
        data['SMA'] = data[column].rolling(window=window).mean()
        data['STD'] = data[column].rolling(window=window).std()
        data['Upper Band'] = data['SMA'] + (data['STD'] * 2)
        data['Lower Band'] = data['SMA'] - (data['STD'] * 2)
        
        plt.figure(figsize=(12,6))
        plt.plot(data[column], label=column)
        plt.plot(data['SMA'], label='SMA')
        plt.plot(data['Upper Band'], label='Upper Band')
        plt.plot(data['Lower Band'], label='Lower Band')
        plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.1)
        plt.title(f'Bollinger Bands for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def plot_macd(self, data: pd.DataFrame, column: str, ticker: str, short_window: int=12, long_window: int=26, signal_window: int=9):
        data['Short EMA'] = data[column].ewm(span=short_window, adjust=False).mean()
        data['Long EMA'] = data[column].ewm(span=long_window, adjust=False).mean()
        data['MACD'] = data['Short EMA'] - data['Long EMA']
        data['Signal Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()

        plt.figure(figsize=(12,6))
        plt.plot(data['MACD'], label='MACD', color = 'blue')
        plt.plot(data['Signal Line'], label='Signal Line', color='red')
        plt.title(f'MACD for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('MACD')
        plt.legend()
        plt.show()
        
