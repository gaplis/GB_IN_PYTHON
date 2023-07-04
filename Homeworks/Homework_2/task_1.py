# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX = 16


def translate_to_hex(num: int) -> str:
    result = []
    hex_nums = {0: 0, 1: 1, 2: 2, 3: 3,
                4: 4, 5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 'a', 11: 'b',
                12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    while num > 0:
        result.append(str(hex_nums[num % HEX]))
        num //= HEX
    return "".join(result[::-1])


number: int = int(input("Введите число: "))
num_hex: str = translate_to_hex(number)

print(f"Число: {number}\n"
      f"Шестнадцатеричное представление: 0x{num_hex}\n"
      f"Проверочное: {hex(number)}")
