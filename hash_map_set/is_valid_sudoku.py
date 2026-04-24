def is_valid_sudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    box = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):

            current = board[i][j]

            if(current=='.'):
                continue
            

            box_index = (i // 3) * 3 + (j // 3)

            if(current in rows[i] or current in cols[j] or current in box):
                return False
            
            rows[i].add(current)
            cols[j].add(current)
            box[box_index].add(current)


    return True




board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board)) 