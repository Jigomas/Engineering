import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin  = 19
timer = 1
reps = 3

GPIO.setup (pin, GPIO.OUT)

for i in range (reps):
    GPIO.output(pin, 1)
    time.sleep (1)
    GPIO.output(pin, 0)
    time.sleep (1)

GPIO.cleanup()
