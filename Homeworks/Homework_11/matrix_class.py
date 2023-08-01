class Matrix:
    def __init__(self, matrix):
        """
        Конструктор класса
        :param matrix: Двумерный список
        """
        self.matrix = matrix

    def print_matrix(self):
        """Выводим матрицу на экран"""
        for row in self.matrix:
            print(*row)

    def __eq__(self, other):
        """
        Сравнение матриц путём сравнения.
        :param other: Объект класса Matrix
        :return: Boolean True/False
        """
        if self.matrix != other.matrix:
            return False
        return True

    def __add__(self, other):
        """
        Складывание матриц путём поэлементного сложения.
        Складывать матрицы можно только если количество рядов и столбцов совпадает.
        :param other: Объект класса Matrix
        :return: Новый объект класса Matrix, в случае равенства входных матриц или поднимает ошибку ValueError.
        """
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Матрица неправильного размера")
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                raise ValueError("Матрица неправильного размера")
        new_matrix = []
        for row_self, row_other in zip(self.matrix, other.matrix):
            new_matrix.append([*map(lambda x: sum(x), zip(row_self, row_other))])
        return Matrix(new_matrix)

    def __mul__(self, other):
        """
        Умножение матриц путём поэлементного умножения.
        Умножать матрицы можно только когда количество столбцов первой матрицы совпадает с количеством строк во второй.
        :param other: Объект класса Matrix
        :return: Новый объект класса Matrix, в случае равенства входных матриц или поднимает ошибку ValueError.
        """
        if len(self.matrix[0]) == len(other.matrix):
            new_matrix = []
            for row_self in self.matrix:
                temp = []
                for col_other in zip(*other.matrix):
                    temp.append(sum(map(lambda x: x[0] * x[1], zip(row_self, col_other))))
                new_matrix.append(temp)
            return Matrix(new_matrix)
        raise ValueError("Матрица неправильного размера")

    def __pow__(self, power):
        """
        Возведение матрицы в степень путём умножения на себя указанное количество раз
        :param power: Степень
        :return: Новый объект класса Matrix
        """
        new_matrix = Matrix(self.matrix.copy())

        for _ in range(power - 1):
            new_matrix = self * new_matrix

        return new_matrix