def is_valid_sudoku(board):

    seen = set()

    for i in range(9):
        for j in range(9):

            current = board[i][j]

            if current == ".":
                continue

            row = (current,i)
            col = (current,j)
            box= (current,(i//3)*3 +(j//3))

            if row in seen or col in seen or box in seen:
                return False
            
            seen.add(row)
            seen.add(col)
            seen.add(box)

    return True