import pandas as pd
import numpy as np
import yfinance as yf

tickers = ['AAPL', 'MSFT', 'GOOGL', 'NVDA']
start_date = '2022-01-01'
end_date = '2024-01-01'

df = yf.download(tickers, start=start_date, end=end_date)

adj_close = df['Close']
returns = adj_close.pct_change().dropna()

mean_returns = returns.mean()
daily_volatility = returns.std()

annual_returns = mean_returns * 252
annual_volatility = daily_volatility * np.sqrt(252)

sharpe_ratio = annual_returns / annual_volatility

cum_returns = (1 + returns).cumprod()
peaks = cum_returns.cummax()
drawdown = (cum_returns - peaks) / peaks
max_drawdown = drawdown.min()

correlation_matrix = returns.corr()

metrics_df = pd.DataFrame({
    'Annual Return': annual_returns,
    'Annual Volatility (Risk)': annual_volatility,
    'Sharpe Ratio': sharpe_ratio,
    'Max Drawdown': max_drawdown
})

formatted_df = metrics_df.copy()
formatted_df['Annual Return'] = (formatted_df['Annual Return'] * 100).round(2).astype(str) + '%'
formatted_df['Annual Volatility (Risk)'] = (formatted_df['Annual Volatility (Risk)'] * 100).round(2).astype(str) + '%'
formatted_df['Max Drawdown'] = (formatted_df['Max Drawdown'] * 100).round(2).astype(str) + '%'
formatted_df['Sharpe Ratio'] = formatted_df['Sharpe Ratio'].round(2)

print("\n" + "="*70)
print("             QUANTITATIVE RISK & PERFORMANCE METRICS             ")
print("="*70)
print(formatted_df)
print("="*70)

print("\n--- Correlation Matrix ---")
print(correlation_matrix.round(3))