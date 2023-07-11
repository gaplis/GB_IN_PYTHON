# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение, лучше многострочное (почему?)

def gen():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            yield 'FizzBuzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif i % 5 == 0:
            yield 'Buzz'
        else:
            yield i


# it = iter(gen())
# print(next(it))
# print(next(it))
# print(next(it))

# for i in gen():
#     print(i)

print(*('FizzBuzz' if i % 3 == 0 and i % 5 == 0
    else 'Fizz' if i % 3 == 0
    else 'Buzz' if i % 5 == 0
    else i for i in range(0, 101)), sep='\n')

# gen = ('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, 101))