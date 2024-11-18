import RPi.GPIO as GPIO
from time import sleep

red_pin = 23

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_pin, GPIO.OUT)

c = 0

while True:
	GPIO.output(red_pin, True)
	sleep(1.0*c)

	GPIO.output(red_pin, False)
	sleep(1.0*(1.0-c))

	if c < 1.0:
		c = c + 0.1
