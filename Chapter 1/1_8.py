import random 

def main():
    m, n = 5, 4
    matrix = [[random.randint(0, 20) for x in range(n)] for y in range(m)]

    print matrix
    print solution(m, n, matrix)

def solution(m, n, matrix):
    col_zero = False
    row_zero = False

    for i in range(m):
        if matrix[i][0] == 0:
            col_zero = True
            break

    for i in range(n):
        if matrix[0][i] == 0:
            row_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        if matrix[i][0] == 0:
            matrix = clear_col(matrix, i, n)

    for i in range(1, n):
        if matrix[0][i] == 0:
            matrix = clear_row(matrix, i, m)

    if row_zero:
        matrix = clear_col(matrix, 0, n)

    if col_zero:
        matrix = clear_row(matrix, 0, m)

    return matrix

def clear_row(matrix, c, m):
    for i in range(m):
        matrix[i][c] = 0

    return matrix

def clear_col(matrix, r, n):
    for i in range(n):
        matrix[r][i] = 0

    return matrix

if __name__ == '__main__':
    main()
