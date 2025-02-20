import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#leds   = [2, 3, 4, 17, 27, 22, 10, 9]
dac    = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1, 1,  0, 0, 0, 0, 0,  0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range (8):
    GPIO.output(dac[i], number[i])
time.sleep (15)

GPIO.output(dac, 0)
GPIO.cleanup()
