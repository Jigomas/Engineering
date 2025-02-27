import RPi.GPIO as GPIO
from time import sleep

def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return [0, 0, 0, 0, 0, 0, 0, 0]

    binary_list = [0] * 8
    index = 0
    while decimal_number > 0:
        binary_list[index] = decimal_number % 2
        decimal_number //= 2
        index += 1

    binary_list.reverse()
    return binary_list

dac_pins = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_pins, GPIO.OUT)
GPIO.setwarnings(False)

increase = True
value = 0

try:
    signal_period = float(input("Введите период сигнала: "))

    while True:
        GPIO.output(dac_pins, decimal_to_binary(value))

        if value == 0:
            increase = True
        elif value == 255:
            increase = False

        value += 1 if increase else -1
        sleep(signal_period / 512)
    
except ValueError:
    print("Некорректный ввод периода!")

finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()
    print("Конец работы программы.")
