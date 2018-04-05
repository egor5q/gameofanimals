# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
from datetime import datetime, timedelta
import random
import threading
import info
import test
from telebot import types
from emoji import emojize
from pymongo import MongoClient

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
whitelist=[441399484,55888804]

werewolf=['Село', 'Камень', 'Ковбой', 'Стрелок', 'Колдун', 'Самоубийца', 
          'Провидец', 'Очевидец', 'Алкоголик', 'Проклятый', 'Принц', 'ЧЛП', 'Ангел',
          'Детектив', 'Дикий ребенок', 'Купидон', 'Двойник', 'Мэр']

client1=os.environ['database']
client=MongoClient(client1)
db=client.gameofanimals
user=db.users
mob=db.mobs
token=db.tokens

def createmob(token, creatorid):
    return{'name':None,
           'token':token,
           'creator':creatorid,
           'attack':1,
           'speed':1,
           'foodmax':25,
           'food':25,
           'luck':0,
           'createtime':datetime.now(),
           'level':0
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
      x=user.find_one({'userid':call.from_user.id})
      if x['mobs']>0 and x['userid'] not in whitelist:
            bot.send_message(call.from_user.id, 'Ваш лимит: 1 существо. Обращайтесь к создателю')
      else:
        token=tokengen()
        user.update_one({'userid':call.from_user.id},{'$inc':{'mobs':1}})
        mob.insert_one({'mob':createmob(token, call.from_user.id)})
        medit('Отлично! Вы создали существо. Его токен:\n'+str(token), call.from_user.id, call.message.message_id)
        
@bot.message_handler(commands=['update'])    
def up(m):
    try:
      mob.update_many({}, {'$set':{'sredn':0, 'kolvo':0}})
    except:
        pass
        
                    
                                                                                         

@bot.message_handler(commands=['name'])
def name(m):
    text=m.text.split(' ')
    print(text)
    if len(text)==3:
      x=mob.find_one({'mob.token':int(text[1])})
      if x['mob']['creator']==m.from_user.id:
                mob.update_one({'mob.token':int(text[1])}, {'$set':{'mob.name':text[2]}})
                bot.send_message(m.from_user.id, 'Вы успешно изменили имя существа на '+text[2]+'!')
    else:
       bot.send_message(m.from_user.id, 'Используйте следующий формат:\n*/name token имя*\nГде *token* - токен вашего существа, а *имя* - имя, которое вы хотите ему примвоить', parse_mode='markdown')
            

 

@bot.message_handler(commands=['info'])
def info(m):
    text=m.text.split(' ')
    print(text)
    if len(text)==2:
     try:
      x=mob.find_one({'mob.token':int(text[1])})
      if x['mob']['creator']==m.from_user.id:
              q=mob.find_one({'mob.token':int(text[1])})
              q=q['mob']
              data=datetime.now() 
              daynow=data.day
              hournow=data.hour
              day=q['createtime'].day
              hour=q['createtime'].hour
              time=[daynow-day, hournow-hour]
              if time[1]<0:
                    time[1]=hour-hournow
                    time[0]-=1
              print(data)
              if q['name']==None:
                name='Без имени'
              else:
                name=q['name']
              bot.send_message(m.from_user.id,'Токен: '+str(q['token'])+'\n'+'Имя: '+name+'\nУровень: '+str(q['level'])+'\nЕда: '+str(q['food'])+'/'+str(q['foodmax'])+'\n'+'Возраст: '+str(time[0])+' Дней и '+str(time[1])+' часов')
     except:
        pass
    else:
        bot.send_message(m.from_user.id, 'Используйте следующий формат:\n*/info token*\nГде *token* - токен вашего существа', parse_mode='markdown')
            
            
@bot.message_handler(commands=['start'])
def create(m):
        if user.find_one({'userid':m.from_user.id}) is None:
            user.insert_one({'userid':m.from_user.id,
                           'mobs':0,
                           'tokens':{}
                          })
        x=user.find_one({'userid':call.from_user.id})
           if x['mobs']>0 and x['userid'] not in whitelist:
               bot.send_message(call.from_user.id, 'Ваш лимит: 1 существо. Обращайтесь к создателю')
           else:
              token=tokengen()
              user.update_one({'userid':call.from_user.id},{'$inc':{'mobs':1}})
              mob.insert_one({'mob':createmob(token, call.from_user.id)})
              bot.send_message(m.from_user.id, 'Вы попали в игру "название_игры"! для начала вам даётся ваше первое существо. Вот его токен: '+str(token), reply_markup=Keyboard)
              
    
               
            

       
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)      
        

        
if __name__ == '__main__':
  bot.polling(none_stop=True)



