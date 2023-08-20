import numpy as np

def row_correct(sudoku: np.ndarray, row_no: int) -> bool:
    row = sudoku[row_no]
    unique_non_zero = np.unique(row[row != 0])
    return len(unique_non_zero) == np.sum(row != 0)

def column_correct(sudoku: np.ndarray, column_no: int) -> bool:
    col = sudoku[:, column_no]
    unique_non_zero = np.unique(col[col != 0])
    return len(unique_non_zero) == np.sum(col != 0)

def block_correct(sudoku: np.ndarray, row_no: int, column_no: int) -> bool:
    block = sudoku[row_no:row_no+3, column_no:column_no+3]
    unique_non_zero = np.unique(block[block != 0])
    return len(unique_non_zero) == np.sum(block != 0)

def sudoku_grid_correct(sudoku: list) -> bool:
    sudoku = np.array(sudoku)
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
    
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if not block_correct(sudoku, i, j):
                return False
                
    return True

if __name__ == '__main__':
    sudoku1 = np.array([
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ])

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = np.array([
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ])

    print(sudoku_grid_correct(sudoku2))

