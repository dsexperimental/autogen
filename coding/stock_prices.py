# filename: stock_prices.py
import yfinance as yf
from datetime import datetime

# Define the ticker symbols for META and TESLA
meta_ticker = "META"
tesla_ticker = "TSLA"

# Get the current year
current_year = datetime.now().year

# Define the start and end dates for the year
start_date = f"{current_year}-01-01"
end_date = f"{current_year}-12-31"

# Retrieve the stock data for the start and end dates
meta_data = yf.download(meta_ticker, start=start_date, end=end_date)
tesla_data = yf.download(tesla_ticker, start=start_date, end=end_date)

# Get the price at the start of the year and at the end of the year for META
meta_start_price = meta_data["Adj Close"].iloc[0]
meta_end_price = meta_data["Adj Close"].iloc[-1]

# Get the price at the start of the year and at the end of the year for TESLA
tesla_start_price = tesla_data["Adj Close"].iloc[0]
tesla_end_price = tesla_data["Adj Close"].iloc[-1]

# Calculate the year-to-date gain for META and TESLA
meta_gain = (meta_end_price - meta_start_price) / meta_start_price * 100
tesla_gain = (tesla_end_price - tesla_start_price) / tesla_start_price * 100

# Print the year-to-date gains
print("META Year-to-Date Gain: {:.2f}%".format(meta_gain))
print("TESLA Year-to-Date Gain: {:.2f}%".format(tesla_gain))