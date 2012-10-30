Stock Market Portfolio - Spring 2011
---
#### Stock Portfolio Analysis using ystockquote
Wrapper for Corey Goldberg's `ystockquote.py` module.  
Gets various properties; closing price, adjusted close, highest price etc. in a given time interval.  
`markowitz.m` builds Markowitz's matrix and mean matrix in order to analyze if portfolio is good.  
It could also visualize volume and percent change of a stock in a scatter plot:  
![Alt text](https://raw.github.com/bugra/Stock-Portfolio/master/img/google_stock.png "Google's 01/01/2010 - 31/08/2012")  
It could also does Gaussian Hidden Markov Analysis(with using Scikitlearn) and plots closing price in different hidden states with respect to its volume:  
![Alt text](https://raw.github.com/bugra/Stock-Portfolio/master/img/gaussian_hmm_closing_volume.png "Google's Closing Price with respect to volume(hidden states are color-coded) 10/29/2010, 10/29/2012")




