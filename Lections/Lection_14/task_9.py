import unittest


class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp')  # только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)

    def test_remove(self):
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])
