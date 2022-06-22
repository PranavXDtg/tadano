#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 12748912, #get it from https://my.telegram.org/auth
    api_hash="67a3f9e77251adefb349169eb1466fba", #get it from https://my.telegram.org/auth
    bot_token="5485929757:AAFNYxk9YNqyewZoT73tU-Td4RFZf0xDba4", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
