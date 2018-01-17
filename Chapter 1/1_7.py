length = 4
matrix = [range(length) for x in range(length)]

for i in range(length-1):
    temp = matrix[0][i]
    matrix[0][i] = matrix[length-1-i][0]
    matrix[length-1-i][0] = matrix[length-1][length-1-i]
    matrix[length-1][length-1-i] = matrix[i][length-1]
    matrix[i][length-1] = temp

print matrix
