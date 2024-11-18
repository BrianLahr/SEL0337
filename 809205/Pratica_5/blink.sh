#!/bin/bash

PIN=23

# Exportando o pino
echo $PIN > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio$PIN/direction

# Loop infinito para piscar o LED
while [ 1 ] do
    	echo 1 > /sys/class/gpio/gpio$PIN/value
    	sleep 0.2
 	echo 0 > /sys/class/gpio/gpio$PIN/value
	sleep 0.2

	done
