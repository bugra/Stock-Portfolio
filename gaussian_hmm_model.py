# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:52:06 2012

@author: bugra
"""

import numpy as np
from sklearn.hmm import GaussianHMM
from StockMarketQuotes import StockMarketQuotes
import matplotlib.pyplot as mlp
def gaussian_hmm_model(stock_market_quote, n_components=5):
    close_v = np.asarray(stock_market_quote.get_closing_price())
    volume = np.asanyarray(stock_market_quote.get_volume())
    volume = volume[:-1]
    diff = close_v[1:] - close_v[:-1]
    close_v = close_v[1:]
    X = np.column_stack([diff, volume])
    model = GaussianHMM(n_components, covariance_type="diag")
    model.fit([X])
    hidden_states = model.predict(X)
    
    print "Transition matrix"
    print model.transmat_
    print ""
    
    print "means and vars of each hidden state"
    for i in xrange(n_components):
        print "%dth hidden state" % i
        print "mean = ", model.means_[i]
        print "var = ", np.diag(model.covars_[i])
        print ""
    
    '''Visualization of Closing Price with respect to Volume, clustered by
    hidden states of data
    '''
    fig = mlp.figure()
    ax = fig.add_subplot(111)
    for i in xrange(n_components):
        idx = (hidden_states == i)
        ax.plot(volume[idx], close_v[idx], 'o', label="%dth hidden state" % i)
    ax.legend()
    ax.set_xlabel('Volume of Stock', fontsize=20)
    ax.set_ylabel('Closing Price of Stock', fontsize=20)
    ax.set_title("""Quote's Volume and closing volume change 
                    in different hidden states""")
    ax.grid(True)
    mlp.show()
    
if __name__ == '__main__':
    google = StockMarketQuotes('GOOG','20101029','20121029')
    gaussian_hmm_model(google)