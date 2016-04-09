import telepot

class Doorbell:
    def __init__(self, bot, domoticNodes):
        self.bot = bot
        self.doorbell = domoticNodes.getNode('NodeDoorbell')
        self.users = []

    # Notifiy after period
    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' and message['text'] == '/notify doorbell':

            self.doorbell.setHandler(self.doorlock_handler)
            #poner un handler en el domoticNodes
            userId = message['from']['id']
            #print 'Doorbell enabled for user ' + userId
            self.users.append(userId)




    def doorlock_handler(self, rutaFichero):
        foto = open(rutaFichero, 'rb')
        for user in self.users:
            self.bot.sendMessage(user, "Estan tocando a la puerta")
            self.bot.sendPhoto(user, foto)

