class indicators():
	
	@staticmethod
	def get_rsi(history, period):
		closingPrices = indicators.get_closing_prices(history)
		deltas = [closingPrices[i] - closingPrices[i - 1] for i in range(1, len(closingPrices))]
		gains = [delta if delta > 0 else 0 for delta in deltas]
		losses = [-delta if delta < 0 else 0 for delta in deltas]
		avg_gain = sum(gains[:period]) / period
		avg_loss = sum(losses[:period]) / period
		rsis = []
		for i in range(period, len(deltas)):
			avg_gain = (avg_gain * (period - 1) + gains[i]) / period
			avg_loss = (avg_loss * (period - 1) + losses[i]) / period
			rs = avg_gain / avg_loss if avg_loss != 0 else float('inf')
			rsis.append(100 - (100 / (1 + rs)))
		return rsis[-1] if rsis else None
		
	@staticmethod
	def get_closing_prices(history):
		closingPrices = [x[4] for x in history]
		return closingPrices