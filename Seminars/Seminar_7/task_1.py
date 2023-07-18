# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform


def fill_file(lines, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(lines):
            f.write(f"{randint(-1000, 1000)}|{uniform(-1000, 1000):.2f}\n")

fill_file(7, 'task_1.txt')