import RPi.GPIO as GPIO

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

try:
    while True:
        user_input = input("Введите число от 0 до 255")

        try:
            num = int(user_input)
            if 0 <= num <= 255:
                binary_output = decimal_to_binary(num)
                GPIO.output(dac_pins, binary_output)
                voltage = (num / 255.0) * 3.3
                print(f"Двоичное представление: {binary_output}")
                print(f"Напряжение: {voltage:.2f} В")
            else:
                print("Число должно быть в диапазоне от 0 до 255.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()
