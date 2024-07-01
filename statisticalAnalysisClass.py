import pandas as pd
import numpy as np

class DataAnalyzer:
    def calculate_mean(self, data: pd.DataFrame, column: str) -> float:
        return data[column].mean()

    def calculate_median(self, data: pd.DataFrame, column: str) -> float:
        return data[column].median()

    def calculate_std(self, data: pd.DataFrame, column: str) -> float:
        return data[column].std()

    def calculate_variance(self, data: pd.DataFrame, column: str) -> float:
        return data[column].var()

    def calculate_cagr(self, data: pd.DataFrame, column: str, periods_per_year: int) -> float:
        end_value = data[column].iloc[-1]
        start_value = data[column].iloc[0]
        n_periods = len(data) / periods_per_year
        return (end_value / start_value) ** (1 / n_periods) - 1

    def calculate_daily_return(self, data: pd.DataFrame, column: str) -> pd.Series:
        return data[column].pct_change()

    def calculate_annualized_volatility(self, data: pd.DataFrame, column: str) -> float:
        daily_returns = self.calculate_daily_return(data, column)
        return daily_returns.std() * np.sqrt(252)

    def calculate_sharpe_ratio(self, data: pd.DataFrame, column: str, risk_free_rate: float = 0.0) -> float:
        daily_return = self.calculate_daily_return(data, column)
        excess_return = daily_return - risk_free_rate / 252
        sharpe_ratio = excess_return.mean() / excess_return.std() * np.sqrt(252)
        return sharpe_ratio

    def calculate_beta(self, stock_data, market_data, column):
        stock_return = stock_data[column].pct_change().dropna()
        market_return = market_data[column].pct_change().dropna()
        
        merged_data = pd.concat([stock_return, market_return], axis=1, join='inner')
        stock_return = merged_data.iloc[:, 0]
        market_return = merged_data.iloc[:, 1]

        covariance = np.cov(stock_return, market_return)[0, 1]
        beta = covariance / np.var(market_return)
        return beta

    def calculate_alpha(self, stock_data: pd.DataFrame, market_data: pd.DataFrame, column: str, risk_free_rate: float = 0.0) -> float:
        beta = self.calculate_beta(stock_data, market_data, column)
        stock_return = stock_data[column].pct_change().mean() * 252
        market_return = market_data.mean() * 252
        alpha = stock_return - (risk_free_rate + beta * (market_return - risk_free_rate))
        return alpha

    def calculate_max_drawdown(self, data: pd.DataFrame, column: str) -> float:
        cumulative_return = (1 + data[column].pct_change()).cumprod()
        peak = cumulative_return.cummax()
        drawdown = (cumulative_return - peak) / peak
        max_drawdown = drawdown.min()
        return max_drawdown
