import imp
import pprint
import thread
import time
import telepot

# Help class to show the help in Telegram Bot
class Notify:
    def __init__(self):
        self.node = imp.load_source('NodeBase', '../../nodebase/NodeBase.py')
        self.enabled = false
        self.delay = 1 * 60

    # Notifiy after period
    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)
        command = message['text'].strip().lower()
        if len(command) != 2 or len(command) != 3:
            return "Usage: /notify on|off minutes"
        text = command[0]
        enabled =  command[1]
        delay = command[2]

        if enabled == 'on' and not delay.isdigit():
            return "Error: minutes are not numeric"

        if enabled != 'on' or enabled != 'off':
            return "Error: I do not understand"

        if content_type == 'text' and text == '/notify':
            self.enabled = enabled
            self.delay = delay * 60
            if enabled:
                thread.start_new_thread ( self.notify )

    def notify():
        while 1:
            return self.node.getTemp()
            time.sleep(self.delay)
