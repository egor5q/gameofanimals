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



client1=os.environ['database']
client=MongoClient(client1)
db=client.god
user=db.users
token=db.tokens
mob=db.mobs

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
        
@bot.message_handler(commands=['killall'])
def kill(m):
  if m.from_user.id==441399484:
    mob.remove({})
    token.remove({})
    user.update_many({}, {'$set':{'mobs':0}})
    
    
@bot.message_handler(commands=['xer'])    
def xerr(m):
    F

def feed():  #Каждые х секунд все сущечтва теряют сытость
    food=threading.Timer(30, feed)
    food.start()
    mob.update_many({}, {'$inc':{'mob.food':-1}}) 
    x=mob.find_one({'mob.token':1})
    try:
      print(x['mob']['food'])
    except:
        pass
        
def life():
        t=threading.Timer(1, life)
        t.start()
        x=mob.find({})
        for mobs in x:
            z=act(mobs)
            if z==1:
                
                mob.update_one(mobs, {'$inc':{'mob.food':1}})
           # z=meetup(mobs)
          #  if z!=None:
            #  if z[0]==1:
             #   bot.send_message(mobs['mob']['creator'], 'Ваше существо с токеном '+str(mobs['mob']['token'])+ ' победило в схватке! Теперь его уровень равен '+str(mobs['mob']['level']+1)+ '!\n'+
               #                 'Существо с токеном '+z[1]['mob']['token']+' теряет уровень!')
              #  mob.update_one(z[1], {'inc':{'mob.level':-1}})
        #
             #   mob.update_one(mobs, {'$inc':{'mob.level':1}})
               
            
def meetup(mobs):
    x=random.randint(1,500)
    if x==1:
        z=None
        a=mob.find({})
        while z==None:
          for mobs in a:
            r=random.randint(1,100)
            if r<=0:
             x=random.randint(1,2)
             if x==1:
              return [1, a]
        return[0, a]
        
        
        

        
       
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)      

    
    
def act(mob):
    mob=mob['mob']   
    if mob['food']<mob['foodmax']:
            a=random.randint(1,100)
            if a<=4+mob['luck']:    
                return 1     
            return 0
def tt():
    bot.send_message(441399484, 'Привет ебло')
        
        
if True:
    t=threading.Timer(300, tt)
    t.start()
    
if True:
    life()
if True:
    feed()
        
if __name__ == '__main__':
  bot.polling(none_stop=True)



