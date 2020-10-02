import telebot
from bs4 import BeautifulSoup
from  parser import *
TOKEN = "1000799565:AAFBwOxONfgDFTyDBf46_6OTSZVpD8Pfc5M"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот по доте start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    a,b = parsers( message.text.lower())
    bot.send_message(message.chat.id, a)



bot.polling()
