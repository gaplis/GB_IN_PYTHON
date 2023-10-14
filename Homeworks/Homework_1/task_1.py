# Вывести в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def maths(n, m):
    for i in range(2, 11):
        for j in range(n, m):
            print(f'{j} * {i}', end='')
            if i < 10:
                print(f' = ', end='')
            else:
                print(f'= ', end='')
            if j * i < 10:
                print(f' {j * i}', end='            ')
            else:
                print(f'{j * i}', end='            ')
        print()

maths(2, 6)
print()
maths(6, 10)
