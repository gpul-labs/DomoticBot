#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

def temp():
   """
   Returns temperature in C*
   """
   return '{0:0.2f}'.format(sensor.read_temperature())
def pressure():
   """
   Returns atmosferic pressure in pascals. 1 atm = 101325 Pa
   """
   return '{0:0.2f}'.format(sensor.read_pressure())
def altitude():
   """
   Returns altitude in meters relative to sea level. Temp dependent
   """
   return '{0:0.2f}'.format(sensor.read_altitude())
