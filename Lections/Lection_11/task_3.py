class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


print('Создаем первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаем второй раз')
b = NamedInt(73, 'Лучшее простое число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')
