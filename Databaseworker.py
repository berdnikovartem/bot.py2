import firebase_admin
from firebase_admin import credentials, firestore
from Coin import coin
from Okex import okex
from OKXWebsocketClient import okxWebSocketClient
from Indicators import indicators
from EntryFinder import entryFinder
from TelegramNotifications import telegramBot
from CoinParametersSetup import coinSetup

from werkzeug.security import generate_password_hash, check_password_hash

class databaseWorker:

	def __init__(self):

		if not firebase_admin._apps:
			cred = credentials.Certificate("learningfirebasseapp-firebase-adminsdk-ivqx2-af1e1db6ec.json")
			firebase_admin.initialize_app(cred)

		self.db = firestore.client()

	def createUser(self, login: str, password: str) -> None:
		user_ref = self.db.collection("users").document(login)
		if user_ref.get().exists:
			print("USER ALREADY EXISTS")
		else:
			hashed = generate_password_hash(password)
			user_ref.set({"password": hashed})
			print(f"USER: {login} CREATED SUCCESSFULY")
			

	def logIntoUser(self, login: str, password: str) -> bool:
		users_ref = self.db.collection("users").document(login)
		user = users_ref.get()

		if user.exists:
			user_data = user.to_dict()
			stored_password_hash = user_data.get("password", "")
			if check_password_hash(stored_password_hash, password):
				print("LOGING SUCCESSFULL")
				return True
			else:
				print("WRONG PASSWORD")
				return False
		else:
			print("WRONG USER LOGIN")
			return False	

	def addCoin(self, coin, user_login):
		coin_data = coin.to_dict()
		ticker = coin_data["ticker"].replace("/", "_")
		self.db.collection("users").document(user_login).collection("coins").document(ticker).set(coin_data)

	def update(self, coin, user_login):
		coin_data = coin.to_dict()
		ticker = coin_data["ticker"].replace("/", "_")
		self.db.collection("updates").document(user_login).collection("coins").document(ticker).set(coin_data)

	def storeCoins(self, coins, user_login):
		for coin in coins:
			coin_data = coin.to_dict()
			ticker = coin_data["ticker"].replace("/", "_")  # Firestore doesn’t like "/"
			self.db.collection("users").document(user_login).collection("coins").document(ticker).set(coin_data)

	def readCoins(self, user_login):
		coins = []
		docs = self.db.collection("users").document(user_login).collection("coins").stream()
		for doc in docs:
			data = doc.to_dict()
			c = coin(data["ticker"])

			c.setAmount(data.get("amount", 0))
			c.setBRsi3MIndicatorV(data.get("rsi_3m_bIndicatorV", 0))
			c.setBRSi30MIndicatorV(data.get("rsi_30m_bIndicatorV", 0))
			c.setVolumeTreshhold(data.get("volume_threshhold", 0))
			c.setSurgeMultiplier(data.get("surge_multiplier", 0))
			c.setDcaLevels(data.get("dca_levels", 0))
			c.setDcaPercentageDrop(data.get("dca_percentage_drop", 0))
			c.setTakeProfitPercentage(data.get("take_profit_percentage", 0))
			c.setHammerShadowMultiplier(data.get("hammer_shadow_multiplier", 0))
			c.setSRsi3MIndicatorV(data.get("rsi_3m_sIndicatorV", 0))
			c.setSRsi30MIndicatorV(data.get("rsi_30m_sIndicatorV", 0))
			c.setDcaPercentageRise(data.get("dca_percentage_rise", 0))
			c.setHedgeMultiplier(data.get("hedge_multiplier", 0))

			coins.append(c)

		return coins

	def deleteCoin(self, ticker, user_login):
		# Firestore documents use '_' instead of '/'
		ticker_doc = ticker.replace("/", "_")

		doc_ref = self.db.collection("users").document(user_login).collection("coins").document(ticker_doc)

		# Check if the document exists before deleting
		if doc_ref.get().exists:
			doc_ref.delete()
			print(f"✅ Coin '{ticker}' deleted successfully.")
		else:
			print(f"⚠️ Coin '{ticker}' not found in database.")

	def deleteAllCoins(self, user_login):
		coins_ref = self.db.collection("users").document(user_login).collection("coins")
		docs = coins_ref.stream()
		deleted_count = 0

		for doc in docs:
			doc.reference.delete()
			deleted_count += 1

		print(f"🗑️ Deleted {deleted_count} coins for user '{user_login}'.")