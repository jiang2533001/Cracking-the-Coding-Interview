import random

def main():
    length = 4
    matrix = [[random.randint(0, 15) for x in range(length)] for y in range(length)]
    
    print matrix
    print solution(matrix, length)

def solution(matrix, length):
    for i in range(length-1):
        temp = matrix[0][i]
        matrix[0][i] = matrix[length-1-i][0]
        matrix[length-1-i][0] = matrix[length-1][length-1-i]
        matrix[length-1][length-1-i] = matrix[i][length-1]
        matrix[i][length-1] = temp

    return matrix

if __name__ == '__main__':
    main()
