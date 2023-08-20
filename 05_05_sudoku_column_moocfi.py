# Write your solution here
def column_correct(sudoku: list, column_no: int):

    # Saves the selected column as a list, so that it can be easily checked!   
 
    column_as_list = []
    for row in sudoku:

        column_as_list.append(row[column_no])


    #print('DEBUG: Selected colum as List: ' + str(column_as_list))


    # let's filter out 'zeros', as they are not needed and represent empty field!

    no_zeros_list = []
    for num in column_as_list:
        if num != 0:
            no_zeros_list.append(num)

    #print('DEBUG: Column without zeros: ' + str(no_zeros_list))

    
    # I want to check for duplicates and check if the numbers are between 1 to 9
    #   For that I create a "set" that doesn't allow for duplicate ints in the first place:
    #   --> If len(list) == len(set(list)) : There are no duplicates
    #       Further: the all() function can be used to make sure that numbers are in the correct range

    if len(no_zeros_list) == len(set(no_zeros_list)) and all(1 <= num <= 9 for num in no_zeros_list):
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

    print(column_correct(sudoku, 0)) # expected: False
    #print('------------------')      # Seperator
    print(column_correct(sudoku, 1)) # expected: True
