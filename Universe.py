import CONST as cst
import PLU as plu

"""
Trading Universe

Objective: 
1. Define Trading Universe (Cryptocurrency Options/Futures, Stock Options/Futures, etc.)
2. For Each Unit (Ticker/Currency, Quantity, Priority (0-100))
"""

class Unit(object):
	
	def __init__(self, ticker, quantity, priority = None):
		
		self.ticker = ticker
		self.quantity = quantity
		self.priority = priority

class HistoricalDataWrapper(object):

  	def __init__(self, ticker, frequency):

  		self.ticker = ticker
  		self.frequency = frequency

class TechnicalIndicatorWrapper(object):

 	def __init__(self, indicator, frequency, indArgs, ticker):
 		
 		self.ticker = ticker
 		self.indicator = indicator
 		self.frequency = frequency
 		self.indicatorArgs = indArgs
		
class Universe(object):

	def __init__(self):

		self.units = []
		self.frequency = cst.NOT_SET

	def addUnit(self, ticker, quantity, priority):

		self.units.append(Unit(ticker, quantity, priority))
		self.units.sort(key=lambda u: u.priority, reverse=True)

	def generateHistoricalData(self, frequency):
		
		self.frequency = frequency
		return [HistoricalDataWrapper(unit.ticker, frequency) for unit in self.units]

	def generateTechnicalIndicator(self, indicator, lag, *args, ticker = None): 

		if (ticker == None):
			dataTuple = (indicator, lag)
			return [TechnicalIndicatorWrapper(*dataTuple, args, unit.ticker) for unit in self.units]

		return TechnicalIndicatorWrapper(indicator, lag, args, ticker)
