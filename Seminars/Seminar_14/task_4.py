# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest

from task_1_2 import str_replace


def test_1():
    assert str_replace('asdgaa baga  aga') == 'asdgaa baga  aga'


def test_2():
    assert str_replace('ASDgaa baga  aga') == 'asdgaa baga  aga'


def test_3():
    assert str_replace('asdgaa baga - aga') == 'asdgaa baga  aga'


def test_4():
    assert str_replace('asdgaa baga фыв aga') == 'asdgaa baga  aga'


def test_5():
    assert str_replace('asdGaa baga 123фв agaфаф') == 'asdgaa baga  aga'


if __name__ == '__main__':
    pytest.main(['-v'])
