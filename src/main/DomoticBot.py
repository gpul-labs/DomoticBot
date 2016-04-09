import telepot
from commands.Help import Help
from nodebase import *

class DomoticBot:
    def __init__(self):
        BOT_TOKEN = '129516182:AAFtuM-28DjMPzVHRL0RUzHYPNVZSNpqp8M'
        self.bot = telepot.Bot(BOT_TOKEN)
        self.handlers = [
            #Start(self.bot),
            #Stop(self.bot),
            Help(self.bot),
            #Temp(self.bot),
            ]
        self.bot.notifyOnMessage(self.handle_message)


    def handle_message(self, message):
        print message
        responses = []
        for hanler in self.handlers:
            responses.append(handler.processMessage(message))
        userId = message['userId']
        for response in responses:
            self.bot.sendMessage(userId, response)



