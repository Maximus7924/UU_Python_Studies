def get_matrix(row, column, value):
    matrix = []
    for n in range(row):
        matrix_column = []
        matrix.append(matrix_column)
        for m in range(column):
            matrix_column.append(value)
    return matrix



result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
