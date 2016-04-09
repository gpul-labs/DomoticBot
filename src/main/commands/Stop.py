import telepot

class Stop:
    def __init__(self, bot, users):
        self.bot = bot
        self.users = users

    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        actualUser = ''
        if content_type == 'text' and message['text'] == '/stop':
            actualUser = message['from']['username']
            actualId = message['from']['id']
            self.users.remove({actualId: actualUser})
            return "Hasta pronto " + actualUser
