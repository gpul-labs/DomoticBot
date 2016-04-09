import telepot
from commands.Start import Start
from commands.Stop import Stop
from commands.Help import Help
from nodebase import *

class DomoticBot:
    def __init__(self):
        self.users = []
        BOT_TOKEN = '129516182:AAFtuM-28DjMPzVHRL0RUzHYPNVZSNpqp8M'
        self.bot = telepot.Bot(BOT_TOKEN)
        self.handlers = [
            Start(self.bot, self.users),
            Stop(self.bot, self.users),
            Help(self.bot),
            #Temp(self.bot),
            ]
        self.bot.notifyOnMessage(self.handle_message)


    def handle_message(self, message):
        print message
        responses = []
        for handler in self.handlers:
            responses.append(handler.processMessage(message))
        userId = message['from']['id']
        for response in responses:
            if response:
                self.bot.sendMessage(userId, response)
