# exchange.py - Handles all API interactions with Binance, also stores important endpoint information incase it is referenced elsewhere, by Mc_Snurtle
# imports
import pandas
import yfinance as yf
import time
import requests
import json
from datetime import datetime, timedelta, date

# yfinance pypi / docs can be found here: https://pypi.org/project/yfinance/
price_url = 'https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms=USD'


# api_ver =   # used solely for checking if API is up-to-spec with current release from other files, also may be deprecated


def legacy_get_symbol_price(symbol: str) -> float:
    return float(requests.get(price_url.format(symbol)).json()['USD'])


def get_symbol_price(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    data = ticker.info
    return data['currentPrice']


def get_crypto_price(symbol: str):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval='1m')
    return data['Close'].iloc[-1]


def get_historical(symbol: str, interval, rounding: bool) -> pandas.DataFrame:
    if interval == '1h':
        start = date.today() - timedelta(728)   # 730 DAYS
    elif interval == '90m' or interval == '2m' or interval == '5m' or interval == '15m' or interval == '30m':
        start = date.today() - timedelta(58)  # 60 DAYS
    else:
        start = 'max'  # NO RATELIMIT
    print(interval)
    if isinstance(start, str):
        data = yf.download(tickers=symbol, period=start, interval=interval, rounding=rounding)
    else:
        data = yf.download(tickers=symbol, start=start, end=date.today(), interval=interval, rounding=rounding)
    return data


def check_symbol(symbol: str):
    ticker = yf.Ticker(symbol)
    return ticker.info
