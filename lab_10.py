
def mainDiagonal():
    TheMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sum = 0
    for i in range(len(TheMatrix)):
        sum += TheMatrix[i][i]
    print("Сумма главной диагонали данной матрицы равна:", sum)

mainDiagonal()