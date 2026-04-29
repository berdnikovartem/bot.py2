import time
import math
import socket 
import logging
import json
from datetime import datetime, timedelta
import threading
import asyncio
import logging

from faststream.rabbit import RabbitBroker
from Coin import coin
from Exchange import Exchange
from Okex import okex
from Bitget import bitget
from OKXWebsocketClient import okxWebSocketClient
from Indicators import indicators
from EntryFinder import entryFinder
from TelegramNotifications import telegramBot
from CoinParametersSetup import coinSetup
from Databaseworker import databaseWorker
from User import user
from Auth import auth
from Sender import Sender

#logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

if __name__ == "__main__":
	sui = coin("SUI/USDT") #Exaple of a coin class
	okx = okex() #Example of a exchange class
	indicator = indicators() #Working indicators class (with indicators)
	entryCheck = entryFinder() #Class for finding entries, which uses indicators class
	tgbot = telegramBot() #Class to work with telegram messages

	setup = coinSetup() #Class which gets all posible futures pairs, allows to add coins from that list

	dbw = databaseWorker() #Allows to add coins and log in into user as well as create user
	user = user()
	auth = auth() #Class to allow user to authorize

	#broker = RabbitBroker("amqp://guest:guest@localhost/")  #FOR FUTUTURE POTENTIAL RABBIT APPLICATION
	#sender = Sender()
	#asyncio.run(sender.post_message(broker, "KYS"))

	bg = bitget() #bitget class example Allows to open limit orders at a certain price
	#bg = Exchange("ASD", 'asda', 'adasd', 'adasd') #Example of not impletmented error
	#bg.limitOrder(tgbot, sui.getTicker(), "limit", "buy", (5.5) , 1) #Example of how limit order is placed on a exchange BITGET
	#bg.getSpotCoins(True) #bitget all spot coin list


	log_success, user = auth.authenticate(dbw, user)
		
	chosen_coins_with_parameters = setup.startCoinSetup(bg) #CAN USE COINS FROM BOTH BITGET OR OKX

	#print(chosen_coins_with_parameters)
	#coins = []
	#coins.append(apt) #EXAMPLE OF HOW TO add coin to list in my computer

	#dbw.storeCoins(coins, user.getLogin()) #Example how to store coins in database
	#dbw.deleteAllCoins(user.getLogin()) #Example how to delete coins
	#dbw.deleteCoin(sui.getTicker(), user.getLogin()) #same shit, deletes exact coin by ticker.

	dbw.storeCoins(chosen_coins_with_parameters, user.getLogin()) #example how to store coins
	coins_from_firebase = dbw.readCoins(user.getLogin())
	for coin in coins_from_firebase:
		print(coin.to_dict())
	

	#ws = okxWebSocketClient("sui.getTicker")
	#ws.start()
