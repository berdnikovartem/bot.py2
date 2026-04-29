from TelegramNotifications import telegramBot

class Exchange:
    def __init__(self, name: str, api: str, secret : str, passphrase : str):
        self.__name__ = name
        self.__api__ = api
        self.__secret__ = secret 
        self.__passphrase__ = passphrase

    def limitOrder(self, tgbot: telegramBot, symbol: str, order_type: str, side: str, amount: float, price: float):
        raise NotImplementedError()
    
    def getSpotCoinList():
        raise NotImplementedError()
    
    def getName(self) -> str:
        return self.__name__
    
    def getApi(self) -> str:
        return self.__api__
    
    def getSecret(self) -> str:
        return self.__secret__
    
    def getPassphrase(self) -> str:
        return self.__passphrase__
    
    def setName(self, name: str) -> None:
        self.__name__ = name
    
    def setApi(self, api: str) -> None:
        self.__api__ = api

    def setSecret(self, secret: str) -> None:
        self.__secret__ = secret

    def setPassphrase(self, passphrase: str) -> None:
        self.__passphrase__ = passphrase
 