# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def gen(n):
    count = 0
    start = 2
    inc = 1
    yield start
    while count < n - 1:
        start += inc
        for i in range(2, int(start ** 0.5) + 1):
            if start % i == 0:
                break
        else:
            inc = 2
            count += 1
            yield start

print(*gen(10))