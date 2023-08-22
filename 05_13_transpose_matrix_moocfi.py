# Write your solution here
def transpose(matrix: list):

    transposed = [[0] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[i][j] = matrix[j][i]
    
    matrix[:] = transposed


if __name__ == '__main__':

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(matrix)
    print(matrix)