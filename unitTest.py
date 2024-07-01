import unittest
import pandas as pd
import numpy as np
from dataLoaderClass import DataLoader
from statisticalAnalysisClass import DataAnalyzer
from visualizationClass import DataVisualizer


data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2022', periods=100, freq='D'),
    'Close': np.random.randn(100).cumsum() + 100,
    'Open': np.random.randn(100).cumsum() + 100,
    'High': np.random.randn(100).cumsum() + 100,
    'Low': np.random.randn(100).cumsum() + 100,
    'Volume': np.random.randint(1, 1000, size=100)
})
data.to_csv('test_data.csv', index=False)


class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.data_loader = DataLoader()
    
    def test_load_csv(self):
        data = self.data_loader.load_csv('test_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

        
    def test_load_yfinance(self):
        data = self.data_loader.load_yfinance('AAPL', '2022-01-01', '2022-12-31')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIn('Close', data.columns)

class TestDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data_analyzer = DataAnalyzer()
        self.data = pd.DataFrame({
            'Close': np.random.randn(100).cumsum() + 100
        })
        self.market_data = pd.DataFrame({
            'Close': np.random.randn(100).cumsum() + 100
        })
    
    def test_calculate_mean(self):
        mean = self.data_analyzer.calculate_mean(self.data, 'Close')
        self.assertIsInstance(mean, float)
    
    def test_calculate_cagr(self):
        cagr = self.data_analyzer.calculate_cagr(self.data, 'Close', 252)
        self.assertIsInstance(cagr, float)
    
    def test_calculate_std(self):
        std = self.data_analyzer.calculate_std(self.data, 'Close')
        self.assertIsInstance(std, float)
    
    def test_calculate_variance(self):
        variance = self.data_analyzer.calculate_variance(self.data, 'Close')
        self.assertIsInstance(variance, float)
    
    def test_calculate_sharpe_ratio(self):
        sharpe = self.data_analyzer.calculate_sharpe_ratio(self.data, 'Close')
        self.assertIsInstance(sharpe, float)
    
    def test_calculate_beta(self):
        beta = self.data_analyzer.calculate_beta(self.data, self.market_data, 'Close')
        self.assertIsInstance(beta, float)
    
    def calculate_alpha(self, stock_data, market_data, column):
        stock_return = stock_data[column].pct_change().dropna()
        market_return = market_data[column].pct_change().dropna()
        
        merged_data = pd.concat([stock_return, market_return], axis=1, join='inner')
        stock_return = merged_data.iloc[:, 0]
        market_return = merged_data.iloc[:, 1]

        beta = self.calculate_beta(stock_data, market_data, column)
        alpha = np.mean(stock_return) - beta * np.mean(market_return)
        return float(alpha)

    
    def test_calculate_max_drawdown(self):
        max_drawdown = self.data_analyzer.calculate_max_drawdown(self.data, 'Close')
        self.assertIsInstance(max_drawdown, float)

class TestDataVisualizer(unittest.TestCase):

    def setUp(self):
        self.data_visualizer = DataVisualizer()
        dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
        self.data = pd.DataFrame({
            'Open': np.random.randn(100).cumsum() + 100,
            'High': np.random.randn(100).cumsum() + 100,
            'Low': np.random.randn(100).cumsum() + 100,
            'Close': np.random.randn(100).cumsum() + 100,
            'Volume': np.random.randint(1, 1000, size=100)
        }, index=dates)
        self.ticker = 'AAPL'

    def test_plot_price_series(self):
        try:
            self.data_visualizer.plot_price_series(self.data, 'Close', self.ticker)
        except Exception as e:
            self.fail(f"plot_price_series raised an exception: {e}")

    def test_plot_volume(self):
        try:
            self.data_visualizer.plot_volume(self.data, self.ticker)
        except Exception as e:
            self.fail(f"plot_volume raised an exception: {e}")

    def test_plot_rsi(self):
        try:
            self.data_visualizer.plot_rsi(self.data, self.ticker)
        except Exception as e:
            self.fail(f"plot_rsi raised an exception: {e}")

    def test_plot_moving_average(self):
        try:
            self.data_visualizer.plot_moving_average(self.data, 'Close', window=20, ticker=self.ticker)
        except Exception as e:
            self.fail(f"plot_moving_average raised an exception: {e}")

    def test_plot_candlestick(self):
        try:
            self.data_visualizer.plot_candlestick(self.data, self.ticker)
        except Exception as e:
            self.fail(f"plot_candlestick raised an exception: {e}")

    def test_plot_bollinger_bands(self):
        try:
            self.data_visualizer.plot_bollinger_bands(self.data, 'Close', ticker=self.ticker)
        except Exception as e:
            self.fail(f"plot_bollinger_bands raised an exception: {e}")

    def test_plot_macd(self):
        try:
            self.data_visualizer.plot_macd(self.data, 'Close', ticker=self.ticker)
        except Exception as e:
            self.fail(f"plot_macd raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
