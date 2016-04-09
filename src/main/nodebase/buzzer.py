#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class buzzer:
   def tone(self, freq, duration):
      self.pwm.start(50)
      self.pwm.ChangeFrequency(freq if freq > 0 else 1)
      time.sleep(duration if duration > 0 else .1)
      self.pwm.stop()

   def __init__(self, pin):
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      GPIO.setup(pin, GPIO.OUT)
      self.pwm = GPIO.PWM(pin, 50)
