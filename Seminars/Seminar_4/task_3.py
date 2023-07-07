# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением —  его порядковый номер из диапазона,
# границами которого являются введенные числа.
# Границы диапазона учитывать

# def create_char_dict(st, en):
#     return {chr(i): i for i in range(st, en + 1)}
#
#
# start, end = sorted(map(int, input("Введите два числа через пробел: ").split()))
# print(create_char_dict(start, end))

def create_char_dict(txt):
    min_num, max_num = map(int, txt.split())
    min_num, max_num = min(min_num, max_num), max(min_num, max_num)
    res = {}
    for i in range(min_num, max_num + 1):
        res[chr(i)] = i

    return res


text = input("Введите два числа через пробел: ")
print(create_char_dict(text))