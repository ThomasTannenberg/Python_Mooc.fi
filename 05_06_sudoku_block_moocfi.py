# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):


    # Load numbers from selected block into a list:
    # But we need to extract a 3x3 Block, a for i loop is needed.

    numbers_from_block = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            numbers_from_block.append(sudoku[i][j])

    print('DEBUG: Numbers from Blog: ' + str(numbers_from_block))

    # Remove zeros because they do not matter:
    list_witout_zeros = []
    for num in numbers_from_block:
        if num != 0:
            list_witout_zeros.append(num)
    
    print('DEBUG: Numbers from Blog without zeros: ' + str(list_witout_zeros))

    # Let's check if the new list has all numbers in the range of 1 - 9 by using the all-function
    # Also let's check if the numbers are unique bys using the sort command
    return all(1<= num <= 9 for num in list_witout_zeros) and len(list_witout_zeros) == len(set(list_witout_zeros))




if __name__ == '__main__':
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

    print(block_correct(sudoku, 0, 0))

    print('-----------------------') # Seperation Line

    print(block_correct(sudoku, 1, 2))