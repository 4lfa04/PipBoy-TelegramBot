import requests
import json
import pandas as pd
import telebot
from telebot.types import ReplyKeyboardMarkup
from settings import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)

nombres = []
numeros = []
direcciones = []
locations = []

def numero_telefonico(message):
    msg = bot.send_message(message.chat.id,"Digame cual es el numero")
    return msg
    
    
def registro(message):
    number = message.text
    website = f'https://directorioetecsa.com/api/search?q={number}'
    result = requests.get(website).text
    lista = json.loads(result)
    # print(lista['data'][0]['name'])
    lista = ""
    lista = lista['data']
    if len(lista) > 0:
        for dato in lista:
            nombres.append(dato['name'])
            numeros.append(dato['number'])
            direcciones.append(dato['address'])
            locations.append(dato['location'])
        print(lista)    
    else:
        print(f'No existe ningun {number}')
        
    
    df = pd.DataFrame({'Nombres':nombres,'Numero':numeros})
    bot.send_message(message.chat.id,f"{df}")
    
    #df = pd.DataFrame({'Nombres':nombres,'Numero':numeros,'Direcciones':direcciones,'Ubicacion GPS':locations})
    #df.to_csv('informacion.csv')
    #document = open('informacion.csv')
    #bot.send_document(message.chat.id,document)
    # print(df)

# dh = pd.DataFrame([nombres,numeros,direcciones,locations])
# dh.to_excel('tabla.xlsx')
