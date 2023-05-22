import telebot
import time
import datetime
from settings import *
import threading
from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones
from telebot.types import ForceReply # Es la libreria citar mensajes
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ayuda_mensaje(message):

    test = ReplyKeyboardRemove()
    
    print(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    if message.text == "✉️ Iniciar Sesion":
        print("Ayuda sobre iniciar sesion")
        bot.send_message(message.chat.id, "Ayudando", reply_markup=test)
        