# Напишите функцию для транспонирования матрицы
def flip_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len((matrix[i]))):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


predefined_matrix = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
print(*predefined_matrix, sep="\n")
flip_matrix(predefined_matrix)
print()
print(*predefined_matrix, sep="\n")
