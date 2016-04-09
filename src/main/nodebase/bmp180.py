#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085

class bmp180():
   def temp(self):
      """
      Returns temperature in C*
      """
      return float('{0:0.2f}'.format(self.sensor.read_temperature()))
   def pressure(self):
      """
      Returns atmosferic pressure in pascals. 1 atm = 101325 Pa
      """
      return float('{0:0.2f}'.format(self.sensor.read_pressure()))
   def altitude(self):
      """
      Returns altitude in meters relative to sea level. Temp dependent
      """
      return float('{0:0.2f}'.format(self.sensor.read_altitude()))

   def __init__(self):
      self.sensor = BMP085.BMP085()
