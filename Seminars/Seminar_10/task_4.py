# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания. Используйте импорт класса в новый файл.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

from task_3 import Person


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id_):
        super().__init__(last_name, first_name, middle_name, age)
        self.id_ = id_
        self.access = self._calculate_access()

    def _calculate_access(self):
        return sum(map(int, str(self.id_))) % 7

e1 = Employee('Ivanov', 'Ivan', 'Ivanovich', '30', 123456)
print(e1.access)