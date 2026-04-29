import requests

class telegramBot:

	def __init__(self):
		self.TELEGRAM_TOKEN = '6697943968:AAEmrKxuDfBiDlvAjzx1gXsFUAaNaj7MmvE'
		self.TELEGRAM_CHAT_ID = '782395586'

	def send_telegram_message(self, message):
		url = f'https://api.telegram.org/bot{self.TELEGRAM_TOKEN}/sendMessage'
		data = {'chat_id': self.TELEGRAM_CHAT_ID, 'text': message}
		try:
			requests.post(url, data=data)
		except Exception as e:
			print(f"Error sending telegram message: {e}")