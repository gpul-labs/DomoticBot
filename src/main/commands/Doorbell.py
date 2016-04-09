import telepot

class Doorbell:
    def __init__(self, bot, domoticNodes):
        self.bot = bot
        self.doorbell = domoticNodes.getNode('NodeDoorbell')
        self.users = []

    # Notifiy after period
    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' and message['text'] == '/doorbell':

            self.doorbell.setHandler(self.doorlock_handler)
            #poner un handler en el domoticNodes
            userId = message['from']['id']
            #print 'Doorbell enabled for user ' + userId
            self.users.append(userId)
            return "Te notificaremos de las llamadas al timbre"



    def doorlock_handler(self, rutaFichero):
        for user in self.users:
            self.bot.sendMessage(user, "Estan tocando a la puerta")
            foto = open(rutaFichero, 'rb')
            self.bot.sendPhoto(user, foto)

