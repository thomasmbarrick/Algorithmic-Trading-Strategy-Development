import yfinance

sp500_data = yfinance.download('^GSPC', start='2000-01-01', end='2023-01-01')
sp500_data.to_csv('SP500_data.csv')
