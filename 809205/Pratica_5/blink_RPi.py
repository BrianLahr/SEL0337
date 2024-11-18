import RPi.GPIO as GPIO
from time import sleep

red_pin = 23

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_pin, GPIO.OUT)

while True:
	GPIO.output(red_pin, True)
	sleep(0.5)	
	
	GPIO.output(red_pin, False)
	sleep(0.5)
