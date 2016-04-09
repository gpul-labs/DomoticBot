import telepot

class DomoticBot:

    def __init__(self):
        BOT_TOKEN = 'theToken'
        self.bot = telepot.Bot(BOT_TOKEN)
        self.handlers = []
        bot.notifyOnMessage(self.handle_message)

    def handle_message(self, message):
        for hanler in self.handlers:
            handler.process(message)

def main():
    domotic_bot = DomoticBot()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
