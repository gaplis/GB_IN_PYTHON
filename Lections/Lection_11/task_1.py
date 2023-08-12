class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальных задач
        print(f'Создал {self} со свойствами:\n'
              f'{self.name = },\t{self.equipment = },\t{self.life = }')


print('Создаем первый раз')
u_1 = User('Спенглер')
print('Создаем второй раз')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
print('Создаем третий раз')
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
