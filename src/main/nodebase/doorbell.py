#!/usr/bin/python
import RPi.GPIO as GPIO

class doorbell:
   def isSwitchActive(self):
      return True if GPIO.input(17) else False

   def __init__(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
