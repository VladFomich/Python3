# Напишите функцию для транспонирования матрицы


def print_matrix(mat_for_print):
    for i in mat_for_print:
        print(i)


def matrix_transponce(mat_for_trans):
    trans = [[mat_for_trans[i][j] for i in range(len(mat_for_trans))] for j in range(len(mat_for_trans[0]))]
    return trans

print("\nСимметричная матрица")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transe_matrix = matrix_transponce(matrix)

print("Заданная матрица:")
print_matrix(matrix)
print("Транспонированная матрица:")
print_matrix(transe_matrix)


print("\nНесимметричная матрица")
matrix = [[1, 2], [3, 4], [5, 6]]
transe_matrix = matrix_transponce(matrix)

print("Заданная матрица:")
print_matrix(matrix)
print("Транспонированная матрица:")
print_matrix(transe_matrix)