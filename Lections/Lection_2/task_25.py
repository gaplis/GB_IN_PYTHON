s = input('Введите текст: ')
if s.isdecimal():
    print(bin(int(s)), oct(int(s)), hex(int(s)))
elif s.isascii():
    print('Текст написан в ASCII.')
else:
    print('Текст не целоt число и не написан в ASCII.')