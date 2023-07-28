class Fabric:
    """Фабрика, принимающая класс и возвращающая новый объект такого-же класса"""

    def __init__(self, obj, *args):
        """
        Конструктор класса.
        :param obj: Ссылка на класс
        :param args: Аргументы необходимые для создания нового класса
        """
        self.obj_class = obj
        self.obj_attrs = args

    def do_copy(self):
        """Метод возвращающий новый объект класса на основе входных данных"""
        return self.obj_class(*self.obj_attrs)