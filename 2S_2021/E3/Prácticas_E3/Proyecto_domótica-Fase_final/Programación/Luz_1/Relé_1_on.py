import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
#Controlando relay 18
GPIO.setup(11, GPIO.OUT)


#try:
while True:
    boton = int(input("Instrucción: "))
    if boton==0:
        GPIO.output(11, GPIO.HIGH)
        break;



GPIO.cleanup();
