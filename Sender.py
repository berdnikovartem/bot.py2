#from fastapi import FastAPI
from faststream.rabbit import RabbitBroker, RabbitQueue
import asyncio

""" FOR WORKING WITH localhost\DOCS
#app = FastAPI()
#broker = RabbitBroker("amqp://guest:guest@localhost/")

@app.on_event("startup")
async def start_broker():
    await broker.connect()

@app.on_event("shutdown")
async def stop_broker():
    await broker.close()

@app.post("/update")
async def make_update(update: str):
    await broker.publish(update, queue="updates")
    return {"data": "OK"} #/
"""

class Sender():

    def __init__(self):
        message = ""

    async def post_message(self, broker: RabbitBroker, msg: str):
        await broker.connect()
        
        queue = RabbitQueue("updates")
        
        await broker.declare_queue(queue)
        await broker.publish(msg, queue=queue)
        await asyncio.sleep(1)
        await broker.close()