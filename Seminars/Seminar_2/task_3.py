import math
import decimal
decimal.getcontext().prec = 42

d = int(input('Введите число: '))

l = decimal.Decimal(math.pi * d)
print(l)
s = decimal.Decimal(math.pi * ((d ** 2) / 4))
print(s)