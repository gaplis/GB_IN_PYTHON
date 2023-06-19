# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

from colorama import Fore

count = int(input('Сколько рядов у ёлки?: '))

for i in range(count):
    if i % 2 == 0:
        point = Fore.RED + '*'
    else:
        point = Fore.GREEN + '*'
    print(' ' * (count - (i + 1)) + point * (i * 2 + 1))