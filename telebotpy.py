from Adafruit_IO import Client                           #importing adafruit library
from telegram.ext import Updater,MessageHandler,Filters  #importing telegram libraries
import os                                                #import os to get hidden keys
import random
#get feed key of adafruit feed
feed_key = os.getenv('feed_key') 
#creating a client
aio = Client('uvi', feed_key)  


#lists 
greeting = ["hi","hello","hey"]
tay = ["what can you do?","what will you do?","say about yourself"]
howlist = ["how are you?","how are you"]
finelist = ["fine","great","good"]
light_on = ["turn on the light","turn on light","lights on","light on","its dark here","on the light"]
light_off = ["turn off the light","turn off light","lights off","light off"]
fan_on = ["turn on the fan","turn on fan","fan on","on the fan"]
fan_off = ["turn off the fan","turn off fan","fan off","off the fan"]

#to make the light ON
def ledon(bot,update):
  chat_id = bot.message.chat_id
  photo_url = 'https://cdn.pixabay.com/photo/2019/09/29/22/06/light-bulb-4514505__480.jpg'
  bot.message.reply_text("Light turned on")
  update.bot.sendPhoto(chat_id=chat_id,photo=photo_url)
  aio.send('led', 1)

#to make the light OFF
def ledoff(bot,update):
  chat_id = bot.message.chat_id
  path='https://www.artnews.com/wp-content/uploads/2021/07/AdobeStock_3317413.jpeg'
  bot.message.reply_text("light turned off")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio.send('led', 0)

#make fan ON
def fanon(bot,update):
  chat_id = bot.message.chat_id
  path='https://i.ytimg.com/vi/bXkcJ2wKMh8/maxresdefault.jpg'
  bot.message.reply_text("fan ON panitan")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio.send('fan', 1)

#make fan OFF
def fanoff(bot,update):
  chat_id = bot.message.chat_id
  path='https://i.ytimg.com/vi/wXghy-PJpgo/maxresdefault.jpg'
  bot.message.reply_text("Fan off panitan")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  aio.send('fan', 0)

#to get the status of light
def lightOnorOff(bot,update):
  feedLight = aio.receive('led')
  if(feedLight.value=='1'):
    bot.message.reply_text("ON")
  else:
    bot.message.reply_text("OFF")
  print(feedLight.value)
  
#get status of fan    
def fanOnorOff(bot,update):
  feedFan = aio.receive('fan')
  if(feedFan.value=='1'):
    bot.message.reply_text("ON")
  else:
    bot.message.reply_text("OFF")
  print(feedFan.value)
  
#for invalid commands  
def inval(bot,update): 
  bot.message.reply_text("command not valid")

#greeting 
def greet(bot,update):
  bot.message.reply_text("Hey dude!")
  
    
#about the bot  
def about(bot,update):
  bot.message.reply_text("I can turn on and off the light and fan for you")

def fine(bot,update):
  mes = random.choice(finelist)
  bot.message.reply_text(mes)

def ok(bot,update):
  bot.message.reply_text("Okay!")

                         

def main(bot,update):
  a = bot.message.text.lower()
  print(a)
  if a in light_on:
    ledon(bot,update)
  elif a in light_off:
    ledoff(bot,update)
  elif a in fan_on:
    fanon(bot,update)
  elif a in fan_off:
    fanoff(bot,update)
  elif a in greeting:
    greet(bot,update)
  elif a in tay:
    about(bot,update)
  elif a in howlist:
    fine(bot,update)
  elif a == "ok" or a=="okay":
    ok(bot,update)
  elif a == "light status":
    lightOnorOff(bot,update)
  elif a == "fan status":
    fanOnorOff(bot,update)
  else:
    inval(bot,update)

BOT_TOKEN = os.getenv('BOT_TOKEN')
up = Updater(BOT_TOKEN,use_context=True)
dp = up.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
up.start_polling()
up.idle()
