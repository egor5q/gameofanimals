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

client=MongoClient('mongodb://egor5q:q10egor50010@db-shard-00-00-fej0s.mongodb.net:27017,db-shard-00-01-fej0s.mongodb.net:27017,db-shard-00-02-fej0s.mongodb.net:27017/test?ssl=true&replicaSet=DB-shard-0&authSource=admin')

        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



