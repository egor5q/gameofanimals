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
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

client=MongoClient('mongodb+srv://egor5q:123@db-fej0s.mongodb.net/test')
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



