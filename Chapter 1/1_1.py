def main():
    string = 'zxcvbnmasdfghjklqwertyuiop'

    if len(string) > 128:
        print False
    else:
        print solution_1(string)
        print solution_2(string)

def solution_1(string):
    boolean_list = [None]*128
    for i in range(len(string)):
        index = ord(string[i])
        if boolean_list[index]:
            return False
        else:
            boolean_list[index] = True
    return True

def solution_2(string):
    chart_dict = {}
    for c in string:
        if chart_dict.has_key(c):
            return False
        else:
            chart_dict[c] = 1
    return True

if __name__ == '__main__':
    main()
