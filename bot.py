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


@bot.message_handler(commands=['chlen'])
def c(m):
    bot.send_message(m.chat.id, 'Да да да, я работаю, отъебитесь')

       
if __name__ == '__main__':
  bot.polling(none_stop=True)



