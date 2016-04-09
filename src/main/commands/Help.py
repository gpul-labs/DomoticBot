from config import *
import telepot
import pprint
import time

# Help class to show the help in Telegram Bot
class Help:
    def __init__(self):
        bot = telepot.Bot(BOT_TOKEN)
        bot.notifyOnMessage(self.help)

    def help(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' && message['text'] == '/help':
            print("Este es el bot de Domotica de la Hackathon de GPUL Labs\n")
            # TODO include instructions

#def main():
#    help_bot = Help()
#    help_bot.help()
#    TODO Include message dictionary from Telegram

#if __name__ == '__main__':
#    main()


