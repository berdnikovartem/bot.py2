import json
import websockets
import asyncio
import datetime
import logging
import threading

from websockets.exceptions import ConnectionClosedError

class okxWebSocketClient:

	def __init__(self, symbols, intervals=["3m", "30m"]):
		self.url = "wss://ws.okx.com:8443/ws/v5/public"
		self.symbols = symbols
		self.intervals = intervals
		self.connection = None

	async def main(self):
		while True:
			try:
				async with websockets.connect(
					self.url,
					ping_interval = 20,
					ping_timeout = 60
				) as ws:
					print("Connected " + datetime.datetime.now().isoformat())

					subs = dict(op='subscribe', args=[dict(channel='tickers', instId='ETH-USDT-SWAP')])
					await ws.send(json.dumps(subs))

					async for msg_string in ws:
						try:
							m = json.loads(msg_string)
							ev = m.get('event')

							if ev == 'error':
								code = int(m.get('code', '0'))
								print(f"OKX error {m.get('msg')} code: {code}")

								if code in [60008]:
									print("Terminal shutting down")
									return

						except Exception as e:
							print(e)

						print(msg_string)

			except ConnectionClosedError as e:
				print(e)
			except CancelledError as e:
				print("Websocket shutted down manually")
				return
			except asyncio.CancelledError:
				print("WebSocket cancelled by user")
				if self.connection:
					await self.connection.close()
				raise
			except Exception as e:
				print(e)

			print("Disconected " + datetime.datetime.now().isoformat())
			await asyncio.sleep(3)

	def start(self):
		asyncio.run(self.main())
		#threading.Thread(target=lambda: asyncio.run(self.main()), daemon=True).start()

