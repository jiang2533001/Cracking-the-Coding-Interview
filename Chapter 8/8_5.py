def main():
    num_1 = 5
    num_2 = 9
    product = num_1

    print solution(product, num_1, num_2)

def solution(product, num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    elif num_2 == 1:
        return product
    else:
        return solution(product + num_1, num_1, num_2 - 1)

if __name__ == '__main__':
    main()
