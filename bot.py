import random
import telebot
from telebot.types import Message
#from telebot import apihelper
#apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}
TOKEN = '751008701:AAGs9-J7rntCcjpYW9XreIsosN01-_uh5tM'

bot = telebot.TeleBot(TOKEN)
#751008701:AAGs9-J7rntCcjpYW9XreIsosN01-_uh5tM
smiles = ['😃','😄','😁','😆',	'😍','😘',]

#bot.send_message(204005166, 'привет из скрипта')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	if message.from_user.id == 204005166:
		bot.reply_to(message, 'Привет')
	else:
		bot.reply_to(message, 'Пока')

@bot.message_handler(func = lambda message: True)
def upper(message: Message):
	bot.reply_to(message, random.choice(smiles))



bot.polling()