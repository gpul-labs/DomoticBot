#!/usr/bin/python
import RPi.GPIO as GPIO

class doorbell:
   def isSwitchActive(self):
      return True if GPIO.input(self.pin) else False

   def __init__(self, pin):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
      self.pin = pin
