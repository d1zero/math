import numpy as np
from numpy import random
from scipy.optimize import linear_sum_assignment


# Назначение задачи
class TaskAssignment:

    # Инициализация класса, обязательными входными параметрами являются
    # матрица задач и метод распределения -Венгерский метод.
    def __init__(self, task_matrix, initial_martix, mode):
        self.task_matrix = task_matrix
        self.initial_martix = initial_martix
        self.mode = mode
        if mode == 'Hungary':
            self.min_cost, self.best_solution = self.Hungary(task_matrix)

        # Венгерский метод
    def Hungary(self, task_matrix):
        b = task_matrix.copy()
        # Строка и столбец минус 0
        for i in range(len(b)):
            row_min = np.min(b[i])
            for j in range(len(b[i])):
                b[i][j] -= row_min
        for i in range(len(b[0])):
            col_min = np.min(b[:, i])
            for j in range(len(b)):
                b[j][i] -= col_min
        line_count = 0
        # Когда количество строк меньше длины матрицы, цикл
        while (line_count < len(b)):
            line_count = 0
            row_zero_count = []
            col_zero_count = []
            for i in range(len(b)):
                row_zero_count.append(np.sum(b[i] == 0))
            for i in range(len(b[0])):
                col_zero_count.append((np.sum(b[:, i] == 0)))
                # Нажать порядок (строка или столбец)
            line_order = []
            row_or_col = []
            for i in range(len(b[0]), 0, -1):
                while (i in row_zero_count):
                    line_order.append(row_zero_count.index(i))
                    row_or_col.append(0)
                    row_zero_count[row_zero_count.index(i)] = 0
                while (i in col_zero_count):
                    line_order.append(col_zero_count.index(i))
                    row_or_col.append(1)
                    col_zero_count[col_zero_count.index(i)] = 0
                    # Нарисуйте линию, покрывающую 0, и получите матрицу после
                    # строки минус минимальное значение и столбец плюс
                    # минимальное значение
            delete_count_of_row = []
            delete_count_of_rol = []
            row_and_col = [i for i in range(len(b))]
            for i in range(len(line_order)):
                if row_or_col[i] == 0:
                    delete_count_of_row.append(line_order[i])
                else:
                    delete_count_of_rol.append(line_order[i])
                c = np.delete(b, delete_count_of_row, axis=0)
                c = np.delete(c, delete_count_of_rol, axis=1)
                line_count = len(delete_count_of_row) + \
                    len(delete_count_of_rol)
                # Когда количество строк равно длине матрицы, выскакиваем
                if line_count == len(b):
                    break
                    # Определяем, нужно ли рисовать линию, чтобы покрыть все
                    # нули, если она покрывает, операции сложения и вычитания
                if 0 not in c:
                    row_sub = list(set(row_and_col) - set(delete_count_of_row))
                    min_value = np.min(c)
                    for i in row_sub:
                        b[i] = b[i] - min_value
                    for i in delete_count_of_rol:
                        b[:, i] = b[:, i] + min_value
                    break
        row_ind, col_ind = linear_sum_assignment(b)
        min_cost = self.initial_martix[row_ind, col_ind].sum()
        best_solution = list(self.initial_martix[row_ind, col_ind])
        return min_cost, best_solution


# Сгенерировать матрицу затрат
rd = random.RandomState(10000)
# task_matrix = rd.randint(0, 10, size=(5, 5))
task_matrix = np.matrix([[5, 3, 4, 1],
                         [3, 1, 2, 1],
                         [4, 2, 2, 1],
                         [6, 5, 4, 2]])

matrix_one = task_matrix.copy()
for row in matrix_one:
    max = matrix_one.max()
    for i in range(0, matrix_one.shape[0]):
        row[0, i] -= max
        row[0, i] *= -1
# Используйте метод Венгрии для распределения задач
ass_by_Hun = TaskAssignment(matrix_one, task_matrix, 'Hungary')
print('cost matrix = ', '\n', task_matrix)
print('Назначение задачи по венгерскому методу:')
print('max cost = ', ass_by_Hun.min_cost)
print('best solution = ', ass_by_Hun.best_solution)
