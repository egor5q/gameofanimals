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
mob=db.mobs

def createmob(token, creatorid):
    return{'name':None,
           'token':token,
           'creator':creatorid
          }

def tokengen():
    number=0
    x=token.find({})
    for one in x:
        number+=1
    token.insert_one({'token':number+1})
    return number+1
    

    


@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='yes':
        token=tokengen()
        x=user.find_one({'userid':call.from_user.id})
        user.update_one({'mobs':{'$exists':True}},{'$inc':{'mobs':1}})
        user['tokens'].insert_one({'token':token})
        mob.insert_one({'mob':createmob(token, call.from_user.id)})
        medit('Отлично! Вы создали существо. Его токен:\n'+str(token), call.from_user.id, call.message.message_id)
        
    


@bot.message_handler(commands=['name'])
def name(m):
    x=user.find_one({'userid':m.from_user.id})
    text=m.text.split(' ')
    print(text)
    if len(text)==3:
        da=0
        print('1')
        for t in x['tokens']:
          if text[1]==x['tokens'][t]:
            da=1
        print('2')
        if da==1:
            mob.update_one({'mob'['name']:{'$exists':True}}, {'mob'['name']:text[2]})
            bot.send_message(m.from_user.id, 'Вы успешно изменили имя существа на '+text[2]+'!')

            
            
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
        
       
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)      

    
    



        
if __name__ == '__main__':
  bot.polling(none_stop=True)



