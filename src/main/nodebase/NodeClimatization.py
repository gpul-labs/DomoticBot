#!/usr/bin/python
import RPi.GPIO as GPIO
import Bmp180
import NodeCooler
import NodeHeater

class NodeClimatization:
   def getTemp(self):
      return self.sensor.temp()

   def setTemp(self, temp):
      self.target = temp
      self.power = True
      
   def __init__(self, pinCooler, pinHeater):
      self.sensor = Bmp180.Bmp180()
      self.cooler = NodeCooler.NodeCooler(pinCooler)
      self.heater = NodeHeater.NodeHeater(pinHeater)
      self.power = False

   def initialize(self):
      self.cooler.initialize()
      self.heater.initialize()

   def turnOff(self):
      self.power = False
      self.cooler.setStatus(False)
      self.heater.setStatus(False)

   def update(self):
      self.cooler.update()
      self.heater.update()

      if self.power:
         if self.getTemp() > self.target:
            self.cooler.setStatus(True)
            self.heater.setStatus(False)
         else:
            self.cooler.setStatus(False)
            self.heater.setStatus(True)

   def getName(self):
      return "NodeClimatization"
