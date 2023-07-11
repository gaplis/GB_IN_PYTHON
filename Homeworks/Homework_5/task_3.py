# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci(n):
    fib_1 = fib_2 = 1
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            yield fib_2
        else:
            fib_sum = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_sum
            yield fib_sum


for e, fib in enumerate(fibonacci(10), start=1):
    print(f'F({e}) = {fib}')