from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n 
    и c 120 по 500 c шагом 5 по оси размерности m
    """
    res = []
    for i in range(0, len(X), 4):
        new_row = []
        for j in range(120, 500, 5):
            if j < len(X[i]):
                new_row.append(X[i][j])
            else:
                new_row.append(-1) 
        res.append(new_row)

    return res
    pass


def sum_non_neg_diag(X: List[List[int]]) -> int:
    sum = 0
    flag = False
    s = -1
    for i in range(min(len(X), len(X[0]))): 
        if X[i][i] >= 0:
            sum += X[i][i]
            flag = True  

    if flag == False:
        return s
    else:
        return sum
    pass

def replace_values(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    new_array = deepcopy(X)

    for j in range(len(X[0])):
        column_sum = sum(X[i][j] for i in range(len(X)))
        M = column_sum / len(X)

        for i in range(len(X)):
            if new_array[i][j] < 0.25 * M or new_array[i][j] > 1.5 * M:
                new_array[i][j] = -1

    return new_array
    pass