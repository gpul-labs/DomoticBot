import telepot

class DomoticBot:

    def __init__(self):
        BOT_TOKEN = 'theToken'
        self.bot = telepot.Bot(BOT_TOKEN)
        self.handlers =
        bot.notifyOnMessage(self.handle_message)

    def handle_message(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text':
            print(message['text'])
            #tweet_message(message['text'])


def main():
    tele_tweet_bot = TeleTweetBot()
    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()
