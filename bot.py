# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
import info
import test
from telebot import types
from emoji import emojize
from pymongo import MongoClient

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client=MongoClient('mongodb+srv://egor5q:123@db-fej0s.mongodb.net/test')
db=client.db1
collection=db.coll
        
        





        
if __name__ == '__main__':
  bot.polling(none_stop=True)



