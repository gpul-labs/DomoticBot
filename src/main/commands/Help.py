# encoding: utf-8
import telepot
import pprint
import time

# Help class to show the help in Telegram Bot
class Help:

    def __init__(self, bot):
        self.bot = bot

    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' and message['text'] == '/help':
            the_help = """Este es el bot de Domotica de la Hackathon de GPUL Labs\n
            /start - Inicializa el bot\n
            /help - Muestra la lista de comandos\n
            /stop - Finaliza la sesión del bot\n
            /temp - Fija la temperatura\n
            /notify - Muestra la temperatura cada X minutos\n
            /list - Lista de devices y sus salas\n"""

            print the_help
            userId = message['from']['id']
            self.bot.sendMessage(userId, the_help)

