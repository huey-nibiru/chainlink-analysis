import pandas as pd
import mplfinance as mpf
import yfinance as yf
from os import system

link_df = yf.Ticker("LINK-USD").history(start="2022-01-01", end="2023-01-01")
btc_df = yf.Ticker("BTC-USD").history(start="2022-01-01", end="2023-01-01")
eth_df = yf.Ticker("ETH-USD").history(start="2022-01-01", end="2023-01-01")


mpf.plot(btc_df, type="candle", volume=True)