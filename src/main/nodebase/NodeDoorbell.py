#!/usr/bin/python
import RPi.GPIO as GPIO
import Buzzer
import time
from subprocess import call
import os

class NodeDoorbell:
   def isSwitchActive(self):
      return True if GPIO.input(self.pin) == GPIO.LOW else False

   def __init__(self, pin, pinBuzzer, duration, frequency):
      self.pin = pin
      self.handler = None
      self.state = False
      self.buzzer = Buzzer.Buzzer(pinBuzzer, duration, frequency)

   def takePicture(self):
      name = str(int(time.time())) + ".jpg"
      call(["fswebcam", "-r", "1920x1080", "/tmp/" + name], stdout = open(os.devnull, 'wb'), stderr = open(os.devnull, 'wb') )
      return "/tmp/" + name

   def initialize(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
      self.buzzer.initialize()

   def setHandler(self, handler):
      self.handler = handler

   def update(self):
      if self.state != self.isSwitchActive():
         self.state = not self.state
         if self.state == True:
            self.buzzer.tone()
            filename = self.takePicture()
            if self.handler != None:
               self.handler(filename)
      self.buzzer.update()

   def getName(self):
      return "NodeDoorbell"
