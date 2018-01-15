def main():
    string = 'Tact Coa'
    print solution(string)

def solution(string):
    dirct = {}
    string = string.lower()
    
    for c in string:
        if 97 <= ord(c) and ord(c) <= 122:
            if dirct.has_key(c):
                dirct[c] += 1
            else:
                dirct[c] = 1

    odd_count = 0
    for key in dirct:
        if dirct[key] % 2 is not 0:
            odd_count += 1
            if odd_count > 1:
                return False
    
    return True


if __name__ == '__main__':
    main()
