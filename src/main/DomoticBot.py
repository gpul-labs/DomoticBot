import telepot
from commands import *
from nodebase import *

class DomoticBot:

    def __init__(self):
        BOT_TOKEN = 'theToken'
        self.bot = telepot.Bot(BOT_TOKEN)
        self.handlers = [Start(bot), Stop(bot), Help(bot), Temp(bot)]

        bot.notifyOnMessage(self.handle_message)


    def handle_message(self, message):
        print message
        responses = []
        for hanler in self.handlers:
            responses.add(handler.process(message))
        userId = message['userId']
        for response in responses:
            self.bot.sendMessage(userId, response)

def main():
    domotic_bot = DomoticBot()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
