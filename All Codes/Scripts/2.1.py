import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range (3):
    for j in range(8):
        GPIO.output(leds[j], 1)
        time.sleep (0.2)
        GPIO.output(leds[j], 0)

GPIO.output(leds, 0)
GPIO.cleanup()
