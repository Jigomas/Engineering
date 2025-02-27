import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

pwm_frequency = 1000
pwm_channel = GPIO.PWM(21, pwm_frequency)
pwm_channel.start(0)

try:
    while True:
        duty_cycle = int(input("Введите значение от 0 до 100: "))
        pwm_channel.ChangeDutyCycle(duty_cycle)
        voltage = 3.3 * duty_cycle / 100
        print(f"Напряжение: {voltage:.2f} В")

except ValueError:
    print("Ошибка: введено некорректное значение.")

finally:
    pwm_channel.stop()
    GPIO.output(21, 0)
    GPIO.cleanup()
