# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_a', '_b', '_shape')

    def __init__(self, a, b=None):
        self._a = a
        self._b = b
        self._shape = 'rectangle'
        if not b:
            self._b = a
            self._shape = 'square'

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def shape(self):
        return self._shape

    @a.setter
    def a(self, a):
        if a > 0:
            self._a = a
        else:
            raise ValueError("Длина должна быть положительной")

    @b.setter
    def b(self, b):
        if b > 0:
            self._b = b
        else:
            raise ValueError("Длина должна быть положительной")

    def per(self):
        return 2 * (self._a + self._b)

    def square(self):
        return self._a * self._b


a = Rectangle(4)
print(a.a)
print(a.b)
print(a.shape)
a.a = 5
print(a.a)
print(a.b)
print(a.shape)
# a.b = -5 # ValueError: Длина должна быть положительной