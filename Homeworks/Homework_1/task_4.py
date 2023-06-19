# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

print('Загадано число от 0 до 1000. Угадайте его.')
num = randint(0, 1001)
count = 10
for i in range(count, 0, -1):
    print(f'Осталось {i} попыток.')
    i_num = int(input('Введите число: '))
    if i_num == num:
        print(f'Вы угадали! Это число {num}.')
        break
    else:
        if i_num > num:
            print(f'Загаданное число меньше {i_num}')
        else:
            print(f'Загаданное число больше {i_num}')
else:
    print('Попытки закончились.')