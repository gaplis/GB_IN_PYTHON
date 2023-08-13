# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time


class MyString(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()

        return instance


a = MyString('Строка', 'Автор')
print(f'Строка: {a}, Автор: {a.author}, Время: {a.time}')
print(a)