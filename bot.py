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
pisuks=0
spisok=['Пиздец', 'Бляяяяяя', 'Дороу', 'Кто будет сосать?']

@bot.message_handler(commands=['chlen'])
def c(m):
    bot.send_message(m.chat.id, 'Да да да, я работаю, отъебитесь')

@bot.message_handler(commands=['sasat'])
def sasat(m):
    bot.send_message(m.chat.id, 'О, вы выбрали пункт "сасат"! Вы сасали '+str(random.randint(1, 1000))+' членов!')

def pisuk():
    global pisuks
    pisuks=0
          
@bot.message_handler(content_types=['text'])
def textm(m):
    global pisuks
    if pisuks==1:
        if 'пид' in m.text.lower() or 'п и д' in m.text.lower():
          bot.send_message(m.chat.id, 'Нахуй иди')
          pisuks=0
    z=random.randint(1, 100)
    if z==1:
        speach=random.choice(spisok)
        bot.send_message(m.chat.id, speach)
    x=m.text.lower()
    if 'писюк' in x or 'пасюк' in x or 'п а с ю к' in x or 'п и с ю к' in x:
        pisuks=1
    if 'писюк пид' in x or 'пасюк пид' in x or 'пасюк п и д' in x or 'писюк п и д' in x:
        
        t=threading.Timer(10, pisuk)
        bot.send_message(m.chat.id, 'Нахуй иди')
    elif 'вирт' in x:
        bot.send_message(m.chat.id, 'Я тоже хочу повиртить!')
    elif 'хуй' in x:
        bot.send_message(m.chat.id, 'ВЫ СКАЗАЛИ "ХУЙ"!')
        
        
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



