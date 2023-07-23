# Создайте функцию-замыкание, которая принимает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
import random

rnd_start = 1
rnd_stop = int(input('Введите до какого числа загадывать: '))
find_number = random.randint(rnd_start, rnd_stop)
count = int(input('Введите количество попыток: '))


def numb(n, c):
    def wrapper():
        for i in range(c):
            print(f'Попытка номер {i + 1}')
            u_res = int(input('Попробуйте угадать число: '))
            if u_res == n:
                return f'Вы угадали! Это число {n}'
            elif u_res < n:
                print('Число больше')
            else:
                print('Число меньше')
        return f'Попытки кончились, увы. Это было число {n}'

    return wrapper


result = numb(find_number, count)
print(result())
