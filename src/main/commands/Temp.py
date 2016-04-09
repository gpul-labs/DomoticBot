import imp
import pprint
import thread
import time
import telepot

# Help class to show the help in Telegram Bot
class Temp:
    def __init__(self, bot, domoticNodes):
        self.bot = bot
        self.nodeClimatization = domoticNodes.getNode("NodeClimatization")
        self.nodeClimatization.initialize()

    # Notifiy after period
    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text':
            command = message['text'].lower().split()
            if command[0] != '/temp':
                return ""

            size = len(command)
            if (size != 2):
                return "Usage: /temp temperatura"

            temp = command[1]
            if not temp.isdigit():
                return "Error: temperature are not numeric"

            self.nodeClimatization.setTemp(float(temp))
            self.bot.sendMessage(message['from']['id'], "La temperatura se ha cambiado a " + str(temp))
