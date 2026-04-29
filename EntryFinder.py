from Coin import coin
from Okex import okex
from Indicators import indicators
from datetime import datetime, timedelta

class entryFinder:

	def __init__(self):
		self.scanner = okex()
		self.indicator = indicators()


	def checkForEntry(self, coin, side): #!side=short, side=long
		if coin == None:
			print(f"Coin that got into entryfinder class was empty")	
			return none

		m3 = self.scanner.getGraphHistory(coin.getTicker(), "3m") #3min timeframe history
		m30 = self.scanner.getGraphHistory(coin.getTicker(), "30m") #30min timeframe candles history

		rsi_3m = self.indicator.get_rsi(m3, 14) #getting 3m rsi value
		rsi_30m = self.indicator.get_rsi(m30, 14) #getting 30m rsi value

		volume_check = self.checkingVolume(m3, coin)

		hammer_check = self.checkingHamerPattern(m3, side) # works for buy side only rn

		time_check = self.checkingTimePassed(m3)

		if side:
			if rsi_3m <= coin.getBRsi3MIndicatorV() and rsi_30m <= coin.getBRsi30MIndicatorV() and volume_check and hammer_check and time_check:
				return True
		else:
			if rsi_3m >= coin.getSRsi3MIndicatorV() and rsi_30m >= coin.getSRsi30MIndicatorV() and volume_check and hammer_check and time_check:
				return True

		return False

	def checkingTimePassed(self, history):
		latest_candle = history[-1]
		last_candle_close_time = datetime.utcfromtimestamp(latest_candle[0] / 1000)
		elapsed_time = datetime.utcnow() - last_candle_close_time
		sufficient_time_elapsed = timedelta(minutes=1) <= elapsed_time <= timedelta(minutes=3)
        

	def checkingHamerPattern(self, history, side): #works for any timeframe
		latest_candle = history[-1]
		open_price = latest_candle[1]
		high_price = latest_candle[2]
		low_price = latest_candle[3]
		close_price = latest_candle[4]

		upper_shadow = high_price - max(open_price, close_price)
		lower_shadow = min(open_price, close_price) - low_price
		body_size = abs(close_price - open_price)

		if side:
			hammer_shadow_multiplier = 1
			is_hammer = lower_shadow >= hammer_shadow_multiplier * body_size and upper_shadow <= body_size
		else: 
			shooting_star_multiplier = 1.5
			is_hammer = upper_shadow >= shooting_star_multiplier * body_size and lower_shadow <= body_size	
        
		return is_hammer

	def checkingVolume(self, history, coin):
		volumes = [x[5] for x in history[-3:]] 

		avg_volume = sum(volumes[:-1]) / 2

		latest_volume = volumes[-1]

		surge_condition = latest_volume >= avg_volume * coin.getSurgeMultiplier()

		volume_condition = sum(volumes) >= coin.getVolumeThreshhold() #checking if last few candles are over required minimum volume

		if volume_condition and surge_condition:
			return True
		else:
			return False
