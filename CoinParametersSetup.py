from Coin import coin
from Okex import okex
from OKXWebsocketClient import okxWebSocketClient
from Indicators import indicators
from EntryFinder import entryFinder
from TelegramNotifications import telegramBot
from Exchange import Exchange

class coinSetup:

	@staticmethod
	def startCoinSetup(exchange: Exchange):
		user_coins = []

		coin_list = exchange.getSpotCoinList(False)	#TRUE = user frindly list, FALSE = full tickers
		#print(coin_list)
		while True:
			setup_method = input("Preload(1)/Manual input(2)/Already existing settings(3) ")
	    	
			if setup_method == "2":

				user_input = input("Enter the coin name you want to use (e.g., BTC): ").upper()
				matching_symbol = None

				for s in coin_list:
					if s.startswith(user_input + "/USDT"):
						matching_symbol = s
						break

				if not matching_symbol:
					print(f"Coin '{user_input}' not found in futures markets.")
					continue

				# Create Coin object with valid ticker
				new_coin = coin(matching_symbol)
				print(f"Setting up parameters for {matching_symbol}")
				new_coin.set_parameters()
				user_coins.append(new_coin)

				# Ask if user wants to add another coin
				more = input("Do you want to add another coin? (yes/no): ").lower()
				if more != "yes":
					break

			elif setup_method == "1": 
				print("not ready yet")
			elif setup_method == "3": 
				print("not ready yet")
			else:	
				print("kys")

		return user_coins
