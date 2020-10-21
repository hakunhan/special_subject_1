def multiply_matrices(X, Y):
    result = [[0] * 3, [0] * 3, [0] * 3]

    # iterate through rows of X
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result

def demo_multiply_matrices():
    matrix_x = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    matrix_y = [[10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]]
    result = multiply_matrices(matrix_x, matrix_y)
    for r in result:
        print(r)

if __name__ == '__main__':
    demo_multiply_matrices()