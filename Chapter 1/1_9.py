def main():
    str_1 = 'waterbottle'
    str_2 = 'erbottlewat'

    print solution(str_1, str_2)

def solution(str_1, str_2):
    str_1 += str_1
    return substring(str_1, str_2)

def substring(str_1, str_2):
    if len(str_1) < len(str_2):
        return False
    else:
        for i in range(len(str_1)):
            if str_1[i] == str_2[0]:
                if len(str_1[i:]) < len(str_2):
                    return False
                else:
                    for j in range(len(str_2)):
                        if str_1[i+j] != str_2[j]:
                            break
                    else:
                        return True
        return False

if __name__=='__main__':
    main()
