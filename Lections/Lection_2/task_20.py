DEFAULT = 42
num = int(input('Введите уровень или нолья для значения по умолчанию: '))
level = num or DEFAULT
print(level)