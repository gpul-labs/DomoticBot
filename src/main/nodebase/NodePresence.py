import RPi.GPIO as GPIO

class NodePresence:
   def isPirActive(self):
      return True if GPIO.input(self.pin) else False

   def __init__(self, pin):
      self.pin = pin
      self.state = False
      self.handler = None

   def initialize(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

   def setHandler(self, handler):
      self.handler = handler

   def update(self):
      if self.state != self.isPirActive():
         self.state = not self.state
         if self.handler != None and self.state == True:
            self.handler()

   def getName(self):
      return "NodePresence"
