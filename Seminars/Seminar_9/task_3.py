# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os
from functools import wraps


def save_params(func):
    if os.path.exists(f'{func.__name__}.json'):
        with open(f'{func.__name__}.json', 'r', encoding='utf-8') as read_file:
            result_list = json.load(read_file)
    else:
        result_list = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'args': args,
                  'kwargs': kwargs,
                  'result': func_res}
        result_list.append(result)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as write_file:
            json.dump(result_list, write_file, indent=2)
        return func_res

    return wrapper


@save_params
def sum_num(a, b,):
    return a + b


if __name__ == "__main__":
    print(sum_num(3, 5))
    print(sum_num(32, 56))
    print(sum_num(89, 3))
