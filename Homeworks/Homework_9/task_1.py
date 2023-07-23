# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
import os
from random import randint as rnd
import csv


def start_fsr(path):
    def deco(func):
        def wrapper(*args, **kwargs):
            with open(path, 'r', newline='', encoding='utf-8') as f:
                csv_read = csv.reader(f)
                for i, line in enumerate(csv_read):
                    if i != 0:
                        result = func(*map(int, line), **kwargs)
                        print(result)
            return result

        return wrapper

    return deco


def save_in_json(func):
    func_name = func.__name__
    if os.path.exists(f'{func_name}.json'):
        with open(f'{func_name}.json', 'r', encoding='utf-8') as read_file:
            result_list = json.load(read_file)
    else:
        result_list = []

    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'args': args,
                  'kwargs': kwargs,
                  'result': func_res}
        result_list.append(result)
        with open(f'{func_name}.json', 'w', encoding='utf-8') as write_file:
            json.dump(result_list, write_file, indent=2)
        return func_res

    return wrapper


@start_fsr('task_1.csv')
@save_in_json
def finder_square_root(a=1, b=1, c=1):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 0
    if d == 0:
        if a:
            x1 = x2 = -b / (2 * a)
        else:
            x1 = x2 = 0
    else:
        if a:
            x1 = (-b - d ** 0.5) / (2 * a)
            x2 = (-b + d ** 0.5) / (2 * a)
        else:
            x1 = x2 = 0
    return x1, x2


def random_nums_in_csv(path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(['a', 'b', 'c'])
        for _ in range(100):
            csv_write.writerow([rnd(0, 100), rnd(0, 100), rnd(0, 100)])


random_nums_in_csv('task_1.csv')
finder_square_root()
