#!/usr/bin/python
import RPi.GPIO as GPIO
from subprocess import call
import time
import os

class Camera:
   def takePicture(self):
      name = str(int(time.time())) + ".jpg"
      call(["fswebcam", "-r", "1920x1080", "/tmp/" + name], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb') )
      return "/tmp/" + name

   def initialize(self):
      return
