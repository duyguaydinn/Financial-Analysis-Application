import pandas as pd
from dataLoaderClass import DataLoader
from statisticalAnalysisClass import DataAnalyzer
from visualizationClass import DataVisualizer
import tkinter as tk
from tkinter import filedialog

class ConsoleApp:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_analyzer = DataAnalyzer()
        self.data_visualizer = DataVisualizer()
        self.data = None
        self.ticker = None

    def load_csv(self):
        root = tk.Tk()
        root.withdraw()  
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = self.data_loader.load_csv(file_path)
            if self.data is not None:
                self.ticker = file_path.split('/')[-1].split('.')[0]
                print(f"Data loaded successfully from {file_path}.")
            else:
                print("Failed to load data from CSV.")
        else:
            print("No file selected.")

    def select_stock(self):
        famous_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "FB", "NVDA", "NFLX", "DIS", "V"]
        print("Select a stock:")
        for i, stock in enumerate(famous_stocks, 1):
            print(f"{i}. {stock}")
        choice = int(input("Enter the number of the stock: "))
        if 1 <= choice <= len(famous_stocks):
            return famous_stocks[choice - 1]
        else:
            print("Invalid choice. Please try again.")
            return self.select_stock()

    def load_yfinance(self):
        ticker = self.select_stock()
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        self.data = self.data_loader.load_yfinance(ticker, start_date, end_date)
        if self.data is not None:
            self.ticker = ticker
            print(f"YFinance data loaded successfully for {ticker}.")
        else:
            print("Failed to load data from Yahoo Finance.")

    def calculate_mean(self):
        if self.data is not None and self.ticker is not None:
            mean_value = self.data_analyzer.calculate_mean(self.data, 'Close')
            print(f"The mean Close price for {self.ticker} is: {mean_value}")
        else:
            print("No data loaded.")

    def calculate_cagr(self):
        if self.data is not None and self.ticker is not None:
            cagr_value = self.data_analyzer.calculate_cagr(self.data, 'Close', 252)
            print(f"The CAGR for {self.ticker} is: {cagr_value}")
        else:
            print("No data loaded.")

    def calculate_std(self):
        if self.data is not None and self.ticker is not None:
            std_value = self.data_analyzer.calculate_std(self.data, 'Close')
            print(f"The standard deviation of Close price for {self.ticker} is: {std_value}")
        else:
            print("No data loaded.")

    def calculate_variance(self):
        if self.data is not None and self.ticker is not None:
            variance_value = self.data_analyzer.calculate_variance(self.data, 'Close')
            print(f"The variance of Close price for {self.ticker} is: {variance_value}")
        else:
            print("No data loaded.")

    def calculate_sharpe_ratio(self):
        if self.data is not None and self.ticker is not None:
            sharpe_value = self.data_analyzer.calculate_sharpe_ratio(self.data, 'Close')
            print(f"The Sharpe Ratio for {self.ticker} is: {sharpe_value}")
        else:
            print("No data loaded.")

    def calculate_beta(self):
        if self.data is not None and self.ticker is not None:
            market_data = self.load_market_data()
            if market_data is not None:
                beta_value = self.data_analyzer.calculate_beta(self.data, market_data, 'Close')
                print(f"The Beta Value for {self.ticker} is: {beta_value}")
            else:
                print("Failed to load market data.")
        else:
            print("No data loaded.")

    def calculate_alpha(self):
        if self.data is not None and self.ticker is not None:
            market_data = self.load_market_data()
            if market_data is not None:
                alpha_value = self.data_analyzer.calculate_alpha(self.data, market_data, 'Close')
                print(f"The Alpha Value for {self.ticker} is: {alpha_value}")
            else:
                print("Failed to load market data.")
        else:
            print("No data loaded.")

    def calculate_max_drawdown(self):
        if self.data is not None and self.ticker is not None:
            mdd_value = self.data_analyzer.calculate_max_drawdown(self.data, 'Close')
            print(f"The Maximum Drawdown for {self.ticker} is: {mdd_value}")
        else:
            print("No data loaded.")

    def plot_price_series(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_price_series(self.data, 'Close', self.ticker)
        else:
            print("No data loaded.")

    def plot_volume(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_volume(self.data, self.ticker)
        else:
            print("No data loaded.")

    def plot_rsi(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_rsi(self.data, self.ticker)
        else:
            print("No data loaded.")

    def plot_moving_average(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_moving_average(self.data, 'Close', window=20, ticker=self.ticker)
        else:
            print("No data loaded.")

    def plot_candlestick(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_candlestick(self.data, self.ticker)
        else:
            print("No data loaded.")

    def plot_bollinger_bands(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_bollinger_bands(self.data, 'Close', ticker=self.ticker)
        else:
            print("No data loaded.")

    def plot_macd(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_macd(self.data, 'Close', ticker=self.ticker)
        else:
            print("No data loaded.")

    def load_market_data(self):
        ticker = "^GSPC"
        start_date = input("Enter the start date for market data (YYYY-MM-DD): ")
        end_date = input("Enter the end date for market data (YYYY-MM-DD): ")
        market_data = self.data_loader.load_yfinance(ticker, start_date, end_date)
        return market_data

    def run(self):
        while True:
            print("\nFinancial Analysis Application")
            print("1. Load Data from CSV")
            print("2. Load Data from Yahoo Finance")
            print("3. Calculate Mean")
            print("4. Calculate CAGR")
            print("5. Calculate Standard Deviation")
            print("6. Calculate Variance")
            print("7. Calculate Sharpe Ratio")
            print("8. Calculate Beta")
            print("9. Calculate Alpha")
            print("10. Calculate Max Drawdown")
            print("11. Plot Price Series")
            print("12. Plot Volume")
            print("13. Plot RSI")
            print("14. Plot Moving Average")
            print("15. Plot Candlestick")
            print("16. Plot Bollinger Bands")
            print("17. Plot MACD")
            print("18. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.load_csv()
            elif choice == '2':
                self.load_yfinance()
            elif choice == '3':
                self.calculate_mean()
            elif choice == '4':
                self.calculate_cagr()
            elif choice == '5':
                self.calculate_std()
            elif choice == '6':
                self.calculate_variance()
            elif choice == '7':
                self.calculate_sharpe_ratio()
            elif choice == '8':
                self.calculate_beta()
            elif choice == '9':
                self.calculate_alpha()
            elif choice == '10':
                self.calculate_max_drawdown()
            elif choice == '11':
                self.plot_price_series()
            elif choice == '12':
                self.plot_volume()
            elif choice == '13':
                self.plot_rsi()
            elif choice == '14':
                self.plot_moving_average()
            elif choice == '15':
                self.plot_candlestick()
            elif choice == '16':
                self.plot_bollinger_bands()
            elif choice == '17':
                self.plot_macd()
            elif choice == '18':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
