# 1. Добавьте в пакет, созданный на семинаре шахматный модуль.
#    Внутри него напишите код, решающий задачу о 8 ферзях.
#    Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
#    Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#    Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
#    Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# 2. Напишите функцию в шахматный модуль.
#    Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
#    Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
#    *Выведите все успешные варианты расстановок
from task_module import queen
import sys

for i, res in enumerate(queen.generate_all(), start=1):
    print(f"{i}: {res}")

count = 0
while True:
    result = queen.check_positions(queen.random_positions())
    if result:
        count += 1
        print(f"{count}: {result}")
    if count == 4:
        sys.exit()
