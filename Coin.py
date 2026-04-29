class coin:
	def __init__(self, ticker):
		self.__ticker = ticker
		self.__amount = 0
		self.__rsi_3m_bIndicatorV = 0
		self.__rsi_30m_bIndicatorV = 0
		self.__volume_threshhold = 0
		self.__surge_multiplier = 0
		self.__dca_levels = 0
		self.__dca_percentage_drop = 0
		self.__take_profit_percentage = 0
		self.__hammer_shadow_multiplier = 0
		self.__rsi_3m_sIndicatorV = 0
		self.__rsi_30m_sIndicatorV = 0
		self.__dca_percentage_rise = 0
		self.__hedge_multiplier = 0  

	def set_parameters(self): #manual input
		self.__amount = float(input("Amount for the first order: "))
		self.__rsi_3m_bIndicatorV = float(input("RSI 3M Buy: "))
		self.__rsi_30m_bIndicatorV = float(input("RSI 30M Buy: "))
		self.__volume_threshhold = float(input("Volume threshold: "))
		self.__surge_multiplier = float(input("Surge multiplier: "))
		self.__dca_levels = int(input("DCA levels: "))
		self.__dca_percentage_drop = float(input("DCA drop %: "))
		self.__take_profit_percentage = float(input("Take profit %: "))
		self.__hammer_shadow_multiplier = float(input("Hammer shadow multiplier: "))
		self.__rsi_3m_sIndicatorV = float(input("RSI 3M Sell: "))
		self.__rsi_30m_sIndicatorV = float(input("RSI 30M Sell: "))
		self.__dca_percentage_rise = float(input("DCA rise %: "))
		self.__hedge_multiplier = float(input("Hedge multiplier: "))

	def to_dict(self):
		return {
			"ticker": self.__ticker,
			"amount": self.__amount,
			"rsi_3m_bIndicatorV": self.__rsi_3m_bIndicatorV,
			"rsi_30m_bIndicatorV": self.__rsi_30m_bIndicatorV,
			"volume_threshhold": self.__volume_threshhold,
			"surge_multiplier": self.__surge_multiplier,
			"dca_levels": self.__dca_levels,
			"dca_percentage_drop": self.__dca_percentage_drop,
			"take_profit_percentage": self.__take_profit_percentage,
			"hammer_shadow_multiplier": self.__hammer_shadow_multiplier,
			"rsi_3m_sIndicatorV": self.__rsi_3m_sIndicatorV,
			"rsi_30m_sIndicatorV": self.__rsi_30m_sIndicatorV,
			"dca_percentage_rise": self.__dca_percentage_rise,
			"hedge_multiplier": self.__hedge_multiplier
		}

	def getTicker(self):
		return f"{self.__ticker}"

	def getAmount(self):
		return self.__amount

	def getBRsi3MIndicatorV(self):
		return self.__rsi_3m_sIndicatorV

	def getBRsi30MIndicatorV(self):
		return self.__rsi_30m_sIndicatorV

	def getVolumeThreshhold(self):
		return self.__volume_threshhold

	def getSurgeMultiplier(self):
		return self.__surge_multiplier

	def getDcaLevels(self):
		return self.__dca_levels

	def getDcaPercentageDrop(self):
		return self.__dca_percentage_drop

	def getTakeProfitPercentage(self):
		return self.__take_profit_percentage

	def getHammerShadowMultiplier(self):
		return self.__hammer_shadow_multiplier

	def getSRsi3MIndicatorV(self):
		return self.__rsi_3m_sIndicatorV

	def getSRsi30MIndicatrorV(self):
		return self.__rsi_30m_sIndicatorV

	def getDcaPercentageRise(self):
		return self.__dca_percentage_rise

	def getHedgeMultiplier(self):
		return self.__hedge_multiplier

	def setTicker(self, ticker):
		self.__ticker = ticker

	def setAmount(self, amount):
		self.__amount = amount

	def setBRsi3MIndicatorV(self, value):
		self.__rsi_3m_bIndicatorV = value

	def setBRSi30MIndicatorV(self, value):
		self.__rsi_30m_bIndicatorV = value

	def setVolumeTreshhold(self, value):
		self.__volume_threshhold = value

	def setSurgeMultiplier(self, value):
		self.__surge_multiplier = value

	def setDcaLevels(self, value):
		self.__dca_levels = value

	def setDcaPercentageDrop(self, value):
		self.__dca_percentage_drop = value

	def setTakeProfitPercentage(self, value):
		self.__take_profit_percentage = value

	def setHammerShadowMultiplier(self, value):
		self.__hammer_shadow_multiplier = value

	def setSRsi3MIndicatorV(self, value):
		self.__rsi_3m_sIndicatorV = value

	def setSRsi30MIndicatorV(self, value):
		self.__rsi_30m_sIndicatorV = value

	def setDcaPercentageRise(self, value):
		self.__dca_percentage_rise = value

	def setHedgeMultiplier(self, value):
		self.__hedge_multiplier = value

