import ccxt
import websockets
from TelegramNotifications import telegramBot
from Exchange import Exchange

class okex(Exchange): #NEED TO FIX THIS CLASS LATER(ORDERS WILL NOT WORK RN)

	def __init__(self):
		super().__init__("OKX", '###', '###', '###')

		self.okx = ccxt.okx({
			'apiKey': self.getApi(),
			'secret': self.getSecret(),
			'password': self.getPassphrase(),
			'enableRateLimit': True,
			'options': {
				'defaultType': 'swap'
			}
		})

	def getCurrentPrice(self, symbol):
		return self.okx.fetch_ticker(symbol)['last']

	def getGraphHistory(self, symbol, timeframe):
		return self.okx.fetch_ohlcv(symbol, timeframe, limit=1000)

	def getALLFuturesCoins(self, userFriendly):  #userFriendly if True = (BTC, ETH, ETC), otherwise tickers.
		exchange = ccxt.okx({
		'enableRateLimit': True,
			'options': {
				'defaultType': 'swap'
			}
		})

		raw_markets = exchange.fetch_markets()
		valid_markets = []

		for market in raw_markets:
			if (
				market.get('type') == 'swap' and
				market.get('quote') == 'USDT' and
				market.get('base') is not None and
				market.get('quote') is not None
			):
				valid_markets.append(market['symbol'])

		if not userFriendly : 
			return valid_markets
		else: 
			return self.makeUserFriendlyCoinList(valid_markets)

	def makeUserFriendlyCoinList(self, tickers):
		symbols = [s.split('/')[0] for s in tickers]
		return symbols

	def open_short_position(symbol, amount):
		try:
			ticker = okx.fetch_ticker(symbol)
			entry_price = ticker['last']
			order = okx.create_order(
	            symbol=symbol,
	            type='market',
	            side='sell',
	            amount=amount,
	            params={'posSide': 'short'}
			)
			return entry_price, True
		except Exception as e:
			telegramBot.send_telegram_message(f"Error opening short position for {symbol}: {e}")
			return None, False

	def open_long_position(symbol, amount):
		try:
			ticker = okx.fetch_ticker(symbol)
			entry_price = ticker['last']
			order = okx.create_order(
	            symbol=symbol,
	            type='market',
	            side='buy',
	            amount=amount,
	            params={'posSide': 'long'}
	        )
			return entry_price, True
		except Exception as e:
			telegramBot.send_telegram_message(f"Error opening long position for {symbol}: {e}")
			return None, False

	def close_short_position(symbol, amount):
		try:
			order = okx.create_order(
	            symbol=symbol,
	            type='market',
	            side='buy',
	            amount=amount,
	            params={'posSide': 'short'}
			)
		except Exception as e:
			telegramBot.send_telegram_message(f"Cannot close short {symbol}: {e}")
		return True

	def close_long_position(symbol, amount):
		try:
			order = okx.create_order(
				symbol=symbol,
	        	type='market',
	        	side='sell',
	        	amount=amount,
	        	params={'posSide': 'long'}
			)
		except Exception as e:
			telegramBot.send_telegram_message(f"Cannot close long {symbol}: {e}")
		return True