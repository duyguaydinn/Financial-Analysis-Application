



import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import Calendar
import pandas as pd
from dataLoaderClass import DataLoader
from statisticalAnalysisClass import DataAnalyzer
from visualizationClass import DataVisualizer

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Analysis App")
        self.root.geometry("1200x900")
        self.root.configure(bg="#f0f0f0")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", background="#333", foreground="#fff", font=("Helvetica", 10, "bold"))
        style.map("TButton", background=[("active", "#555")])
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabelFrame", background="#f0f0f0", font=("Helvetica", 12, "bold"))
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))

        self.data_loader = DataLoader()
        self.data_analyzer = DataAnalyzer()
        self.data_visualizer = DataVisualizer()
        self.data = None
        self.ticker = None

        self.create_widgets()

    def create_widgets(self):

        title_label = ttk.Label(self.root, text="Financial Analysis Application", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)


        load_frame = ttk.LabelFrame(self.root, text="Load Data", padding=(20, 10))
        load_frame.pack(fill="x", padx=20, pady=10)

        self.load_button = ttk.Button(load_frame, text="Load CSV", command=self.load_csv)
        self.load_button.grid(row=0, column=0, padx=10, pady=5)

        ttk.Label(load_frame, text="Start Date:").grid(row=0, column=1, padx=(20, 5))
        self.start_date_entry = tk.Entry(load_frame, width=12)
        self.start_date_entry.grid(row=0, column=2, padx=10, pady=5)
        self.start_date_button = ttk.Button(load_frame, text="Select Start Date", command=lambda: self.pick_date(self.start_date_entry))
        self.start_date_button.grid(row=0, column=3, padx=10, pady=5)

        ttk.Label(load_frame, text="End Date:").grid(row=0, column=4, padx=(20, 5))
        self.end_date_entry = tk.Entry(load_frame, width=12)
        self.end_date_entry.grid(row=0, column=5, padx=10, pady=5)
        self.end_date_button = ttk.Button(load_frame, text="Select End Date", command=lambda: self.pick_date(self.end_date_entry))
        self.end_date_button.grid(row=0, column=6, padx=10, pady=5)

        famous_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "FB", "NVDA", "NFLX", "DIS", "V"]
        self.stock_combobox = ttk.Combobox(load_frame, values=famous_stocks)
        self.stock_combobox.set("Select Stock")
        self.stock_combobox.grid(row=0, column=7, padx=10, pady=5)

        self.load_yfinance_button = ttk.Button(load_frame, text="Load YFinance Data", command=self.load_yfinance)
        self.load_yfinance_button.grid(row=0, column=8, padx=10, pady=5)

#ANALYSIS
        analysis_frame = ttk.LabelFrame(self.root, text="Analysis Options", padding=(20, 10))
        analysis_frame.pack(fill="x", padx=20, pady=10)

        self.mean_button = ttk.Button(analysis_frame, text="Calculate Mean", command=self.calculate_mean)
        self.mean_button.pack(side="left", padx=10, pady=5)

        self.cagr_button = ttk.Button(analysis_frame, text="Calculate CAGR", command=self.calculate_cagr)
        self.cagr_button.pack(side="left", padx=10, pady=5)

        self.std_button = ttk.Button(analysis_frame, text="Calculate Std Dev", command=self.calculate_std)
        self.std_button.pack(side="left", padx=10, pady=5)

        self.variance_button = ttk.Button(analysis_frame, text="Calculate Variance", command=self.calculate_variance)
        self.variance_button.pack(side="left", padx=10, pady=5)

        self.sharpe_button = ttk.Button(analysis_frame, text="Calculate Sharpe Ratio", command=self.calculate_sharpe_ratio)
        self.sharpe_button.pack(side="left", padx=10, pady=5)

        self.beta_button = ttk.Button(analysis_frame, text="Calculate Beta", command=self.calculate_beta)
        self.beta_button.pack(side="left", padx=10, pady=5)

        self.alpha_button = ttk.Button(analysis_frame, text="Calculate Alpha", command=self.calculate_alpha)
        self.alpha_button.pack(side="left", padx=10, pady=5)

        self.mdd_button = ttk.Button(analysis_frame, text="Calculate Max Drawdown", command=self.calculate_max_drawdown)
        self.mdd_button.pack(side="left", padx=10, pady=5)
#PLOT
        self.plot_frame = ttk.LabelFrame(self.root, text="Plot Options", padding=(20, 10))
        self.plot_frame.pack(fill="x", padx=20, pady=10)

        self.price_series_button = ttk.Button(self.plot_frame, text="Plot Price Series", command=self.plot_price_series)
        self.price_series_button.pack(side="left", padx=10, pady=5)

        self.volume_button = ttk.Button(self.plot_frame, text="Plot Volume", command=self.plot_volume)
        self.volume_button.pack(side="left", padx=10, pady=5)

        self.rsi_button = ttk.Button(self.plot_frame, text="Plot RSI", command=self.plot_rsi)
        self.rsi_button.pack(side="left", padx=10, pady=5)

        self.moving_average_button = ttk.Button(self.plot_frame, text="Plot Moving Average", command=self.plot_moving_average)
        self.moving_average_button.pack(side="left", padx=10, pady=5)

        self.candlestick_button = ttk.Button(self.plot_frame, text="Plot Candlestick", command=self.plot_candlestick)
        self.candlestick_button.pack(side="left", padx=10, pady=5)

        self.bollinger_button = ttk.Button(self.plot_frame, text="Plot Bollinger Bands", command=self.plot_bollinger_bands)
        self.bollinger_button.pack(side="left", padx=10, pady=5)

        self.macd_button = ttk.Button(self.plot_frame, text="Plot MACD", command=self.plot_macd)
        self.macd_button.pack(side="left", padx=10, pady=5)

    def pick_date(self, entry):
        def print_sel():
            entry.delete(0, tk.END)
            entry.insert(0, cal.selection_get().strftime('%Y-%m-%d'))
            top.destroy()

        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode='day', date_pattern='y-mm-dd')
        cal.pack(pady=20)

        ttk.Button(top, text="Select", command=print_sel).pack(pady=20)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = self.data_loader.load_csv(file_path)
            self.ticker = file_path.split('/')[-1].split('.')[0]
            messagebox.showinfo("Information", "Data loaded successfully")

    def load_yfinance(self):
        ticker = self.stock_combobox.get()
        if ticker == "Select Stock":
            messagebox.showwarning("Warning", "Please select a stock.")
            return
        self.ticker = ticker
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.data = self.data_loader.load_yfinance(ticker, start_date, end_date)
        if self.data is not None:
            messagebox.showinfo("Information", "YFinance data loaded successfully")

    def calculate_mean(self):
        if self.data is not None and self.ticker is not None:
            mean_value = self.data_analyzer.calculate_mean(self.data, 'Close')
            messagebox.showinfo("Mean Value", f"The mean Close price for {self.ticker} is: {mean_value}")

    def calculate_cagr(self):
        if self.data is not None and self.ticker is not None:
            cagr_value = self.data_analyzer.calculate_cagr(self.data, 'Close', 252)
            messagebox.showinfo("CAGR Value", f"The CAGR for {self.ticker} is: {cagr_value}")

    def calculate_std(self):
        if self.data is not None and self.ticker is not None:
            std_value = self.data_analyzer.calculate_std(self.data, 'Close')
            messagebox.showinfo("Standard Deviation", f"The standard deviation of Close price for {self.ticker} is: {std_value}")
    def calculate_variance(self):
        if self.data is not None and self.ticker is not None:
            variance_value = self.data_analyzer.calculate_variance(self.data, 'Close')
            messagebox.showinfo("Variance", f"The variance of Close price for {self.ticker} is: {variance_value}")

    def calculate_sharpe_ratio(self):
        if self.data is not None and self.ticker is not None:
            sharpe_value = self.data_analyzer.calculate_sharpe_ratio(self.data, 'Close')
            messagebox.showinfo("Sharpe Ratio", f"The Sharpe Ratio for {self.ticker} is: {sharpe_value}")

    def calculate_beta(self):
        if self.data is not None and self.ticker is not None:
            market_data = self.load_market_data()
            if market_data is not None:
                beta_value = self.data_analyzer.calculate_beta(self.data, market_data, 'Close')
                messagebox.showinfo("Beta Value", f"The Beta Value for {self.ticker} is: {beta_value}")

    def calculate_alpha(self):
        if self.data is not None and self.ticker is not None:
            market_data = self.load_market_data()
            if market_data is not None:
                alpha_value = self.data_analyzer.calculate_alpha(self.data, market_data, 'Close')
                messagebox.showinfo("Alpha Value", f"The Alpha Value for {self.ticker} is: {alpha_value}")

    def calculate_max_drawdown(self):
        if self.data is not None and self.ticker is not None:
            mdd_value = self.data_analyzer.calculate_max_drawdown(self.data, 'Close')
            messagebox.showinfo("Max Drawdown", f"The Maximum Drawdown for {self.ticker} is: {mdd_value}")

    def plot_price_series(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_price_series(self.data, 'Close', self.ticker)

    def plot_volume(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_volume(self.data, self.ticker)

    def plot_rsi(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_rsi(self.data, self.ticker)

    def plot_moving_average(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_moving_average(self.data, 'Close', window=20, ticker=self.ticker)

    def plot_candlestick(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_candlestick(self.data, self.ticker)

    def plot_bollinger_bands(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_bollinger_bands(self.data, 'Close', ticker=self.ticker)

    def plot_macd(self):
        if self.data is not None and self.ticker is not None:
            self.data_visualizer.plot_macd(self.data, 'Close', ticker=self.ticker)

    def load_market_data(self):
        ticker = "^GSPC"
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        market_data = self.data_loader.load_yfinance(ticker, start_date, end_date)
        return market_data

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()