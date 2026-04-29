from TelegramNotifications import telegramBot
from Exchange import Exchange
import ccxt

class bitget(Exchange):

    def __init__(self):
        
        super().__init__("Bitget","bg_f8d87d88e24b16218dcc2a150cfa7162", "cd3e6dacf6b7ea388638dfca9b1f5c48efcef3725b15a6fe8397f1e07b4b44f7", "zxcvbnm123aQ1")
        
        self.bitget = ccxt.bitget({
            'apiKey': self.__api__,
            'secret': self.__secret__,
            'password': self.__passphrase__,
            'enableRateLimit': True,
        })
    
    def limitOrder(self, tgbot: telegramBot, symbol: str, order_type: str, side: str, amount: float, price: float) -> bool:
        try:
            order = self.bitget.create_order(
                symbol=symbol,
                type=order_type,
                side=side,
                amount=amount,
                price=price
            )
        except Exception as e:
            tgbot.send_telegram_message(f"Unable to open a limit order on Bitget exchange. {symbol}, error {e}")    
        return True
    
    def getSpotCoinList(self, userFriendly):
        # userFriendly=True -> returns ['BTC', 'ETH', ...]
        # userFriendly=False -> returns ['BTC/USDT', 'ETH/USDT', ...]

        exch = ccxt.bitget({
            'enableRateLimit': True,
            'options': {
                'defaultType': 'spot'  # swap for futures
            }
        })

        raw_markets = exch.fetch_markets()
        valid_markets = []

        for market in raw_markets:
            if (
                market.get('type') == 'spot' and
                market.get('quote') == 'USDT' and
                market.get('base') is not None and
                market.get('quote') is not None
            ):
                valid_markets.append(market['symbol'])

        if not userFriendly:
            return valid_markets
        else:
            return self.makeUserFriendlyCoinList(valid_markets)

    def makeUserFriendlyCoinList(self, tickers):
        symbols = [s.split('/')[0] for s in tickers]
        return symbols