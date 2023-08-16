# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import pytest
from rectangle import Rectangle


@pytest.fixture
def data():
    return Rectangle(3, 5)


def test_per(data):
    assert data.per() == 16


def test_square(data):
    assert data.square() == 15


def test_equal(data):
    assert data == Rectangle(3, 5)


if __name__ == "__main__":
    pytest.main(["-v"])
