#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class Buzzer(object):
   def tone(self):
      self.startTime = int(time.time())
      self.pwm.start(50)
      self.pwm.ChangeFrequency(self.frequency if self.frequency > 0 else 1)

   def __init__(self, pin, duration, frequency):
      self.pin = pin
      self.duration = duration
      self.startTime = None
      self.frequency = frequency

   def initialize(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      GPIO.setup(self.pin, GPIO.OUT)
      self.pwm = GPIO.PWM(self.pin, 50)

   def update(self):
      if self.startTime == None:
         return
      if int(time.time()) - self.startTime >= self.duration:
         self.pwm.stop()
         self.startTime = None
