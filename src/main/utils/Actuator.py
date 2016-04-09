import RPi.GPIO as GPIO # libreria para los GPIO
import time

class Actuator:

    __init__(self, pinNumber):
        GPIO.setmode(GPIO.BCM)
        self.pinNumber = pinNumber
        GPIO.setup(pinNumber, GPIO.OUT)

    enablePin(self):
        GPIO.output(pinNumber, True)

    disablePin(self):
        GPIO.output(pinNumber, False)

def main():
    while 1: # Bucle infinito
        actuator = new Actuator(18)
        actuator.enablePin() # enciende el LED
        time.sleep(1) # aguarda 1 segundo
        actuator.disablePin() # apaga el LED
        time.sleep(1) # aguarda 1 segundo


if(__name__ ) == '__main__':
    main()
