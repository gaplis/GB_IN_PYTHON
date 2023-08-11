# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest

import pytest

from task_5 import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(3, 5)

    def test_per(self):
        self.assertEqual(Rectangle(3, 5).per(), 16)

    def test_square(self):
        self.assertEqual(Rectangle(3, 5).square(), 15)

    def test_equal(self):
        self.assertEqual(Rectangle(3, 5), self.rectangle)


if __name__ == "__main__":
    pytest.main(["-v"])
