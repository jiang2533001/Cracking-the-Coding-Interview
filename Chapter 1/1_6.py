def main():
    string = 'aabcccccaaa'

    print solution(string)

def solution(string):
    string = string.lower()
    
    current = string[0]
    count = 1
    compression = ''

    for c in string[1:]:
        if c == current:
            count += 1
        else:
            compression += current + str(count)
            current = c
            count = 1
   
    compression += current + str(count)
    return compression

if __name__ == '__main__':
    main()
