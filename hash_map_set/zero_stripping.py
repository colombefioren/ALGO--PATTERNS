def set_zeroes(matrix):

    rows = set()
    cols = set()

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):

            current = matrix[i][j]

            if(current == 0):
                rows.add(i)
                cols.add(j)

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if i in rows or j in cols:
                matrix[i][j] = 0
    
    return matrix



matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print("Before:", matrix)
set_zeroes(matrix)
print("After:", matrix)