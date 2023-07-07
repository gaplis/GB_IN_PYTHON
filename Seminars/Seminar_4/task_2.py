# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def char_order(txt):
    return sorted([ord(c) for c in set(txt)], reverse=True)


text = input("Введите текст: ")
print(char_order(text))