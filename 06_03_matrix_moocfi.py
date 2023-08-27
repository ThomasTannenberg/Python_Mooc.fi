# helper function to open the file:
# function returns a list with all numbers as row_lists
def read_file():
    matrix_list = []                            # initializing list that will be returned
    matrix_row = []  

    with open('matrix.txt') as matrix_file:     # opens matirx.txt as stream
        for row in matrix_file:                 # goes through each line in the file
                    
            numbers = row.split(',')            # splits each line into a list os numbers (as strings)

            for number in numbers:              # goes through each string-number in the list
                number = int(number)            # converts strings to integers
                matrix_row.append(number)       # appends each 'row' of integers to list

            matrix_list.append(matrix_row)      # appends row-list to new list

    return matrix_list                          # returns list

# helper function to combine each number in list
# when rows do not matter
def combine(matrix: list):
    combined_list = []                          # initializes empty list

    for row in matrix:                          # goes through each line in matrix
        combined_list += row                    # adds each number to list

    return combined_list                        # retunrs list

# returns a list containing the sum of each row in the matrix
def row_sums():
    matrix = read_file()

    row_sums = []                               # initializes list
    sum_helper = 0                              # initializes helper variable
    
    for row in matrix:                          # goes through each line in matrix
        sum_helper = sum(row)                   # calculates sum for each line
        row_sums.append(sum_helper)             # sum for each line is being put into list
  
    return row_sums                             # returns list

# returns the sum of all numbers in matrix
def matrix_sum():
    matrix = combine(read_file())
    return sum(matrix)

# returns the max value in matrix:
def matrix_max():
    matrix = combine(read_file())
    max_value = max(matrix)
    return max_value

if __name__ =="__main__":
#    print(read_file())
    print(row_sums())
    print(matrix_max())
    print(matrix_sum())