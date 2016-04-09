from config import *
import telepot
import pprint
import time

# Help class to show the help in Telegram Bot
class Help:
    def __init__(self):

    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' && message['text'] == '/help':
            print("Este es el bot de Domotica de la Hackathon de GPUL Labs\n")
            print("/start - Inicializa el bot\n")
            print("/help - Muestra la lista de comandos\n")
            print("/stop - Finaliza la sesión del bot\n")
            print("/temp - Fija la temperatura\n")
            print("/notify - Muestra la temperatura cada X minutos\n")
            print("/list - Lista de devices y sus salas\n")

        
