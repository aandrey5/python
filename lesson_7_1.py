# 1. Реализовать класс Matrix (матрица). Об
def div():
    print('-'*60)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = str()
        for el in self.matrix:
            n = ' '.join(map(str, el))  # получаем список текстовых эелементов первого списочка матрицыб, собираем строку через пробел из элементов первого списочка матрицы
            my_str += n + '\n'  # наращиваем строку через \n для красивого вывода матрицы, накапливаем в строку my_str
        return f'{my_str}'

    def __add__(self, other):
        if len(self.matrix[0]) > len(other.matrix[0]):
            result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        else:
            result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for i in range(len(other.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
            #print(f'не поддерживаются разноразрядные матрицы')


matrix_1 = Matrix([[2, 8, 8], [8, 4, 9], [7, 8, 1]])
matrix_2 = Matrix([[7, 1, 8, -8], [2, 6, 8, -1], [3, 2, 9, 8]])
matrix_3 = Matrix([[7, 1], [2, 6], [3, 2]])

div()
print('ПРОГРАММА СЛОЖЕНИЯ МАТРИЦ\nПОДДЕРЖИВАЮТСЯ МАТРИЦЫ РАЗНОГО РАЗМЕРА')
div()
print('Матрица первая: matrix_1 ')
div()
print(matrix_1)
div()
print('Матрица вторая: matrix_2 ')
div()
print(matrix_2)

div()
print('Результат сложения матриц: 1 и 2')
div()
print(matrix_1 + matrix_2)
div()
print('Матрица третья: matrix_3 ')
div()
print(matrix_3)
div()

print('Результат сложения матриц: 3 и 1')
div()
print(matrix_3 + matrix_1)
div()
