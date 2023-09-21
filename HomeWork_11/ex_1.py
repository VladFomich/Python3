# Создайте класс Матрица. Добавьте методы для:  
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


class Matrix:

    def __init__(self, rows, cols):

        self.rows = rows

        self.cols = cols

        self.data = [[0] * cols for _ in range(rows)]  



    def print_matrix(self):

        for row in self.data:

            print(*row)



    def __eq__(self, other):

        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:

            return False

        for i in range(self.rows):

            for j in range(self.cols):

                if self.data[i][j] != other.data[i][j]:

                    return False

        return True



    def __add__(self, other):

        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:

            raise ValueError("Матрицы должны быть одинакового размера")

        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):

            for j in range(self.cols):

                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result



    def __mul__(self, other):

        if not isinstance(other, Matrix) or self.cols != other.rows:

            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):

            for j in range(other.cols):

                for k in range(self.cols):

                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result
        


m1 = Matrix(2, 2)

m1.data = [[1, 2], [3, 4]]

print("Матрица m1:")

m1.print_matrix()



m2 = Matrix(2, 2)

m2.data = [[5, 6], [7, 8]]

print("Матрица m2:")

m2.print_matrix()



print("Равенство: \nm1 == m2 ?", m1 == m2)


m3 = m1 + m2

print("Сложение: \nМатрица m3 = m1 + m2:")

m3.print_matrix()



m4 = m1 * m2

print("Умножение: \nМатрица m4 = m1 * m2:")

m4.print_matrix()