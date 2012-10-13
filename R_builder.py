# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:31:05 2012

@author: bugra
"""
from StockMarketQuotes import StockMarketQuotes
import numpy as np
import scipy.io as sio

google = StockMarketQuotes('GOOG','20100101','20120831')
microsoft = StockMarketQuotes('MSFT','20100101','20120224')
apple = StockMarketQuotes('AAPL','20100101','20120224')
#netflix = StockMarketQuotes('NFLX','20100101','20120224')
yahoo = StockMarketQuotes('YHOO','20100101','20120224')
#ibm = StockMarketQuotes('NYSE','20100101','20120224')
pfizer = StockMarketQuotes('PFE','20100101','20120224')
morganStanley = StockMarketQuotes('MS','20100101','20120224')
#oppenheimerHoldings = StockMarketQuotes('OPY','20100101','20120224')
mcDonald =  StockMarketQuotes('MCD','20100101','20120224')
#caterPillar = StockMarketQuotes('CAT','20100101','20120224')
cocaCola = StockMarketQuotes('KO','20100101','20120224')


def write_mean():
	means = np.matrix([google.calculate_mean(), microsoft.calculate_mean(), apple.calculate_mean(),\
					    yahoo.calculate_mean(), mcDonald.calculate_mean(), cocaCola.calculate_mean(),\
					    pfizer.calculate_mean(), morganStanley.calculate_mean()]) 
	sio.savemat('means.mat',{'M':means})
	return means


def build_R():
	R = np.zeros([8,8,530],float)
	for ii in range(0, 530):
		vector = np.matrix([google.calculate_difference_from_mean()[ii], microsoft.calculate_difference_from_mean()[ii], apple.calculate_difference_from_mean()[ii], yahoo.calculate_difference_from_mean()[ii],mcDonald.calculate_difference_from_mean()[ii], cocaCola.calculate_difference_from_mean()[ii], pfizer.calculate_difference_from_mean()[ii], morganStanley.calculate_difference_from_mean()[ii]])
		vectorTranspose = vector.transpose()
		smallR = (vectorTranspose*vector)
		R[:,:,ii] = smallR
	sio.savemat('R1.mat',{'R':R})
	return R
print build_R()
build_R()