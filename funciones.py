import telebot
import time
import datetime
from settings import *
import threading
from telebot.types import ReplyKeyboardMarkup # Es la libreria para crear botones
from telebot.types import ForceReply # Es la libreria citar mensajes

import help_responses
import horarias

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def start(message):
    bot.send_message(message.chat.id, f"🧑‍🚀 Saliendo de la criogenizacion!",'html')
    if True:
        bot.send_message(message.chat.id, "Veo que no estas registrado, por favor registrate para acceder a mas funciones \n/signup: Registrarte\n/help: Muestra un mensaje de ayuda")
    else:
        bot.send_message(message.chat.id, "Hola de nuevo, almirante")
    
def help(message):
    foto = open('./assets/animated_stickers/help_meme.tgs',"rb")
    bot.send_document(message.chat.id,foto)
    markup = ReplyKeyboardMarkup(
      one_time_keyboard=True,
      input_field_placeholder="Pulsa Un Boton",
      resize_keyboard=True
    )
    markup.add("✉️ Iniciar Sesion",)
    markup.add("🌐 Pagina Web")
    
    msg = bot.send_message(message.chat.id, f"Con Gusto te puedo ayudar\nDime, que duda tienes?",reply_markup=markup)
    # bot.register_next_step_handler(msg, help_responses.ayuda_mensaje,msg)
    # bot.register_next_step_handler(msg, ayuda_mensaje)
    # markup = ReplyKeyboardMarkup(one_time_keyboard=True,input_field_placeholder="Pulsa Un Boton",resize_keyboard=True)
    # markup.add("Hombre","Mujer")
    # msg = bot.send_message(message.chat.id, "Arrancando Funcion de botonera", reply_markup=markup)
    return msg
    
def signup(message):
    print(message.text)
    
    bot.send_message(message.chat.id, f"👋 Hola <b>{message.chat.first_name}</b>\nSoy tu Asistente Personal...",'html')
    mensaje = bot.send_message(message.chat.id, "⚙️ Voy a cargar todas mis funciones...")
    hilo_horas = threading.Thread(name="hilo_bot",target=horarias.start_temporizador,args=(message,))
    hilo_horas.start()
    bot.edit_message_text("⚙️ Todas mis funciones estan cargadas",message.chat.id,mensaje.id)