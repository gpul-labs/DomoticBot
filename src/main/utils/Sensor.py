import RPi.GPIO as GPIO # libreria para los GPIO
import time

class Sensor:

    __init__(self, pinNumber):
        GPIO.setmode(GPIO.BCM)
        self.pinNumber = pinNumber
        GPIO.setup(pinNumber, GPIO.IN)

    read(self):
        GPIO.input(pinNumber)

def main():
    while 1: # Bucle infinito
        sensor = new Sensor(18)
        actuator.enablePin() # enciende el LED
        time.sleep(1) # aguarda 1 segundo
        actuator.disablePin() # apaga el LED
        time.sleep(1) # aguarda 1 segundo


if(__name__ ) == '__main__':
    main()
