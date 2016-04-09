import imp
import pprint
import thread
import time
import telepot

# Help class to show the help in Telegram Bot
class Notify:
    def __init__(self, bot, domoticNodes):
        self.threadId = -1
        self.bot = bot
        self.nodeClimatization = domoticNodes.getNode("NodeClimatization")
        self.nodeClimatization.initialize()
        self.stop = True
        self.delay = (float)(1 * 60)

    # Notifiy after period
    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text':
            command = message['text'].lower().split()
            if command[0] != '/notify':
                return ""

            size = len(command)
            if (size != 2 and size != 3):
                return "Usage: /notify [ on minutes | off ]"

            if command[1] != 'on' and command[1] != 'off':
                return "Usage: /notify [on minutes | off]"

            enabled = (command[1] == 'on')
            if size == 3:
                delay = command[2]

            if enabled and not delay.isdigit():
                return "Error: minutes are not numeric"

            if enabled:
                self.delay = float(delay) * 60.0
                self.stop = False
                self.threadId = thread.start_new_thread( self.notify, (message,))
		return "Te avisare cada " + delay + " minutos de la temperatura "
            else:
		self.threadId.exit()
                self.stop = True
		return "Has detenido las notificaciones de temperatura"

    def notify(self, message):
        while not self.stop:
            temp = self.nodeClimatization.getTemp()
            print self.delay
            self.bot.sendMessage(message['from']['id'], "La temperatura es " + str(temp))
            time.sleep(float(self.delay))
