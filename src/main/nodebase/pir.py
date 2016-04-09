#!/usr/bin/python
import RPi.GPIO as GPIO

class pir:
   def isPirActive(self):
      return True if GPIO.input(23) else False

   def __init__(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
