# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def count(num):
    def deco(func):
        results = []

        def wrapper(*args, **kwargs):
            for i in range(num):
                results.append(func(*args, **kwargs))
                print(f'Функция запущена {i + 1} раз')
            return results

        return wrapper

    return deco


@count(5)
def calc(a, b):
    return a + b


if __name__ == "__main__":
    print(calc(1, 2))
