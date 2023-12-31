# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def check_input():
    while True:
        num = input('Введите число от 1 до 999: ')
        if num.isdecimal() and 0 < (res := int(num)) < 1000:
            return res
        print('Введено неверное значение! Попробуйте еще раз!')

n = check_input()
match n:
    case n if n // 10 < 1:
        result = n ** 2
    case n if n // 100 < 1:
        result = (n // 10) * (n % 10)
    case _:
        result = (n // 100) + ((n % 100) // 10 * 10) + ((n % 100) % 10 * 100)
print(result)