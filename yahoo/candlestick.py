import pandas as pd
import mplfinance as mpf
import yfinance as yf

link_df = yf.Ticker("LINK-USD").history(start="2022-01-01", end="2023-01-01")
btc_df = yf.Ticker("LINK-USD").history(start="2022-01-01", end="2023-01-01")
eth_df = yf.Ticker("LINK-USD").history(start="2022-01-01", end="2023-01-01")
