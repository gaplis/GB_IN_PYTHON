def check_input():
    while True:
        try:
            num = int(input('Введите год: '))
            if num < 0:
                raise ValueError
        except ValueError:
            print('Введено неверное значение! Попробуйте еще раз!')
            continue
        break
    return num

year = check_input()
gregorian = 1582
print('Обычный' if year < gregorian or year % 4 != 0 or year % 100 == 0 and year % 400 != 0 else 'Високосный')