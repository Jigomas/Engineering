import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

pin  = 26
checker = 19

GPIO.setup (checker,  GPIO.OUT)
GPIO.setup (pin,       GPIO.IN)

GPIO.output(checker, GPIO.input(pin))
