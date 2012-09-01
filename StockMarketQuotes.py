import ystockquote
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
""" 
Wrapper for ystockquote.
Class that uses ystockquote and returns information of stock prices in a given time interval. 
Need to give the beginning date and end date for the time interval, and of course the stock name.
It can return stock's opening, closing, highest, lowest, volume, adjusted close values. 
It could also calculate gain when you invest in the stock price in the beginning date to end date, also how much
it deviates from the mean. 
write_mean() and build_R() are helper functions for Matlab(.m) files in this directory. 
They help to create Markowitz Matrix for stock portfolio.
@ Bugra
"""
class StockMarketQuotes:

    def __init__(self, stock_name, beginning_date, end_date):
        self.stock_name = stock_name
        self.beginning_date = beginning_date
        self.end_date = end_date
        self.data = ystockquote.get_historical_prices(self.stock_name,self.beginning_date,self.end_date) 
		
    def get_date(self):	
        quote_date = []
        for ii in range(1, len(self.data)):
            quote_date.append(float(self.data[ii][0]))
        return quote_date
		
    def get_opening_price(self):
        opening_price = []
        for ii in range(1, len(self.data)):	
            opening_price.append(float(self.data[ii][1]))
        return opening_price
        
    def get_closing_price(self):
        closing_price = []
        for ii in range(1, len(self.data)):	
            closing_price.append(float(self.data[ii][4]))
        return closing_price
		
    def get_highest_price(self):
        highest_price = []
        for ii in range(1, len(self.data)):
            highest_price.append(float(self.data[ii][2]))
        return highest_price
		
    def get_lowest_price(self):
        lowest_price = []
        for ii in range(1, len(self.data)):
            lowest_price.append(float(self.data[ii][3]))
        return lowest_price
		
    def get_volume(self):
        volume = []
        for ii in range(1, len(self.data)):
            volume.append(float(self.data[ii][5]))
        return volume
		
    def get_adjusted_close(self):
        adjusted_close = []
        for ii in range(1, len(self.data)):
            adjusted_close.append(float(self.data[ii][6]))
        return adjusted_close
		
    def calculate_gain(self):
        gain = []
        for ii in range(0, (len(self.data)-1)):	
            gain.append(float((self.get_highest_price()[ii] - self.get_adjusted_close()[ii])/ self.get_adjusted_close()[ii]))
        return gain
		
    def calculate_mean(self):
        mean = sum(self.get_adjusted_close()) / (len(self.get_adjusted_close()))
        return mean
		
    def calculate_difference_from_mean(self):
        diff = []
        for ii in range(0, (len(self.data)-1)):
            diff.append(float(self.get_highest_price()[ii] - self.calculate_mean()))
        return diff
		
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
    
visualize_stock_price(google)

  
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
