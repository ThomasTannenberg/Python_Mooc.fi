def row_correct(sudoku: list, row_no: int):
    # load in rows only:
    row = sudoku[row_no]
#    print(row)
    
    # Filter out zeros, they are empty and do not need to be checked.
    non_zero_numbers_in_row = []
    for num in row:
        if num != 0:
            non_zero_numbers_in_row.append(num)
#    print(set(non_zero_numbers_in_row))

    # Check if numbers are unique!
    #   First remove any duplicate numbers with the set-command. If the length of the list == the length of the "set" --> there are no duplicates
    #   Simultansouely the numbers need to be between 1 - 9: the all command can be used!
    if len(non_zero_numbers_in_row) == len(set(non_zero_numbers_in_row)) and all(1 <= num <= 9 for num in non_zero_numbers_in_row):
        return True
    else:
        return False



if __name__ == "__main__":

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))  # expected: True
    print(row_correct(sudoku, 1))  # expected: False

    # This took me forever... I am doing something wrong!