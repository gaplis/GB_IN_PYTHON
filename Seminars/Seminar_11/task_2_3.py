# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.
class Archive:
    """Реализация паттерна Singleton"""

    _instance = None

    def __new__(cls, *args):
        """
        Проверка на наличие экземпляра

        :param num: Номер ячейки
        :param value: Содержимое ячейки
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive = []
        else:
            cls._instance.archive.append((cls._instance.num, cls._instance.value))
        return cls._instance

    def __init__(self, num, value):
        self.num = num
        self.value = value

    def __str__(self):
        return f'{self.num}, {self.value}, {self.archive}'

    def __repr__(self):
        return 'Archive({}, {})'.format(self.num, (self.value, "'" + self.value + "'")[isinstance(self.value, str)])


c = Archive(42, "Data")
# print(c)
print(f'{c.num = }, {c.value = }, {c.archive = }')
d = Archive(55, "Data2")
print(f'{c.num = }, {c.value = }, {c.archive = }')
print(f'{d.num = }, {d.value = }, {d.archive = }')
# help(c)
e = Archive(22, "Data3")
print(f'{e.num = }, {e.value = }, {e.archive = }')

print(f"{e = }")