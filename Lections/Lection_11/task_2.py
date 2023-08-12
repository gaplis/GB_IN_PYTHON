class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance


print('Создаем первый раз')
u_1 = User('Спенглер')
print('Создаем второй раз')
u_2 = User('Венкман')
print('Создаем третий раз')
u_3 = User(name='Стэнц')
