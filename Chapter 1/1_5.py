def main():
    str_1 = 'pale'
    str_2 = 'bake'

    print solution(str_1, str_2)

def solution(str_1, str_2):
    if len(str_1) >= len(str_2):
        length = len(str_1)
    else:
        length = len(str_2)

    for i in range(length):
        if i == length - 1:
            return True
        else:
            if str_1[i] is not str_2[i]:
                if len(str_1) != len(str_2):
                    return str_1[i+1:-1] == str_2[i:-1]
                else:
                    return str_1[i+1:-1] == str_2[i+1:-1]
    return False

if __name__ == '__main__':
    main()
