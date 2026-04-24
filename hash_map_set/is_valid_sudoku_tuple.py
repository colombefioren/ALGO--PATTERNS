def is_valid_sudoku(board):

    seen = set()

    for i in range(9):
        for j in range(9):

            current = board[i][j]

            if current == ".":
                continue

            row = f"{current} in row {i}"
            col = f"{current} in col {j}"
            box= f"{current} in box {(current,(i//3)*3 +(j//3))}"

            if row in seen or col in seen or box in seen:
                return False
            
            seen.add(row)
            seen.add(col)
            seen.add(box)

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