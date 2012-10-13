# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:34:15 2012

@author: bugra
"""
from StockMarketQuotes import StockMarketQuotes
import numpy as np
import matplotlib.pyplot as plt

def visualize_stock_price(quote, days=100):
    delta = np.diff(quote.get_adjusted_close()) / quote.get_adjusted_close()[:-1]
    first_volume = quote.get_volume()[0]
    vol =  [(15 * x/first_volume) ** 2 for x in quote.get_volume()]
    volume = vol[:-2]
    temp = [0.003 * ( float(x) / y) for x, y in zip(quote.get_closing_price(), quote.get_opening_price())]
    close = temp[:-2]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(delta[:-1], delta[1:], c=close, s=volume, alpha=0.75)
    ax.set_xlabel(r'$\Delta_i$', fontsize=20)
    ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=20)
    ax.set_title("Google's Volume and percent change")
    ax.grid(True)
    plt.show()
    
google = StockMarketQuotes('GOOG','20100101','20120831')    
visualize_stock_price(google)