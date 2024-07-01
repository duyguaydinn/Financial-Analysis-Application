import pandas as pd
import yfinance as yf

class DataLoader:
    def load_csv(self, file_path):
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except pd.errors.EmptyDataError:
            print("No data in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_yfinance(self, ticker, start, end):
        try:
            data = yf.download(ticker, start=start, end=end)
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
