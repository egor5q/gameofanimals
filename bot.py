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
whitelist=[441399484]


client=MongoClient('mongodb://egor5q:123@db-shard-00-00-fej0s.mongodb.net:27017,db-shard-00-01-fej0s.mongodb.net:27017,db-shard-00-02-fej0s.mongodb.net:27017/test?ssl=true&replicaSet=DB-shard-0&authSource=admin')
db=client.god
user=db.users
token=db.tokens



def tokengen():
    number=0
    x=token.find({})
    for one in x:
        number+=1
    tokens.insert_one({'token':number+1})
    return number+1
    

    


@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='yes':
        token=tokengen()
        bot.send_message(call.from_user.id, 'Отлично! Вы создали существо. Его токен:\n'+token)
        
    





@bot.message_handler(commands=['create'])
def create(m):
        if user.find_one({'userid':m.from_user.id}) is None:
            user.insert_one({'userid':m.from_user.id,
                           'mobs':0,
                           'tokens':{}
                          })
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="Да", callback_data='yes'))
        Keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data='no'))
        bot.send_message(m.from_user.id, 'Хотите создать существо?', reply_markup=Keyboard)
        

        
        
def life():
        t=threading.Timer(1, life)
        t.start()
        
       
        

    
    



        
if __name__ == '__main__':
  bot.polling(none_stop=True)



