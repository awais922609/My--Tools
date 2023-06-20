# -*- coding: utf-8 -*-
"""Crypto Guessing 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o41Nyax_q4OT_0f5So6mXE7DJ4zEd7dT
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Get the data for Bitcoin
url = "https://api.coingecko.com/api/v3/coins/ilcapo/market_chart"
params = {
    "vs_currency": "usd",
    "days": 365
}
response = requests.get(url, params=params)
data = response.json()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])

# Convert timestamp to datetime and price to numeric
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df["price"] = pd.to_numeric(df["price"])

# Calculate the RSI
window_length = 14
close_prices = df["price"]
delta = close_prices.diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window_length).mean()
avg_loss = loss.rolling(window_length).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# Calculate the moving averages
ma_5 = close_prices.rolling(5).mean()
ma_10 = close_prices.rolling(10).mean()

# Calculate the Bollinger Bands
upper_band = ma_10 + 2 * (ma_10 - ma_5)
lower_band = ma_10 - 2 * (ma_10 - ma_5)

# Use the technical indicators to predict the future trends
last_rsi = rsi.iloc[-1]
if last_rsi < 30:
    trend = "The cryptocurrency is oversold and is likely to go up in price."
elif last_rsi > 70:
    trend = "The cryptocurrency is overbought and is likely to go down in price."
else:
    trend = "The cryptocurrency is neither overbought nor oversold and is likely to continue its current trend."

print(trend)

# Predict the future trends
predicted_prices = ma_10 + (upper_band - ma_10) * (rsi - 30) / 40

# Plot the predicted future trends
plt.plot(df["timestamp"], ma_10, label="MA 10")
plt.plot(df["timestamp"], upper_band, label="Upper Band")
plt.plot(df["timestamp"], lower_band, label="Lower Band")
plt.plot(df["timestamp"], predicted_prices, label="Predicted Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Ilcapo Price with Predicted Trends")
plt.legend()
plt.show()