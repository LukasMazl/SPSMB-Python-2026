from matrix import plus, zeros, eyes, format, T, multiply


if __name__ == "__main__":
    matrix_a = [
        [1, 2, 0],
        [0, 1, 2],
        [0, 1, 1]
    ]

    matrix_b = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    #matrix_c = plus(matrix_a, matrix_b)

    #   2, 1, 2
    #   1, 2, 1
    #   1, 1, 2

    #format(T(matrix_c))
    format(multiply(matrix_a, matrix_b))
