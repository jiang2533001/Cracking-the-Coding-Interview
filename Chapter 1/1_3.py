def main():
    string = 'Mr John Smith  '
    size = 13

    print solution(string, size)

def solution(string, size):
    revision = ''
    for i in range(size):
        if string[i] is ' ':
            revision += '%20'
        else:
            revision += string[i]
    
    return revision

if __name__ == '__main__':
    main()
