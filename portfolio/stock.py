import pandas as pd
import quandl
import pandas_datareader as pdr # Use to import data from the web
import datetime # use for start and end dates
import matplotlib.pyplot as plt


def makeStock(ticker, start, end):
    return pdr.get_data_google(ticker, datetime.datetime(start), datetime.datetime(end))
