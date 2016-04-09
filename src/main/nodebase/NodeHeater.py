#!/usr/bin/python
import RPi.GPIO as GPIO

class NodeHeater:
   def getStatus(self):
      return GPIO.input(self.pin)

   def setStatus(self, state):
      GPIO.output(self.pin, GPIO.HIGH if state else GPIO.LOW)

   def __init__(self, pin):
      self.pin = pin

   def initialize(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)

      GPIO.setup(self.pin, GPIO.OUT)
      GPIO.output(self.pin, GPIO.LOW)

   def update(self):
      return
