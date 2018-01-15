def main():
    str_1 = 'dogg'
    str_2 = 'godd'

    if len(str_1) is not len(str_2):
        print False
    else:
        print solution(str_1, str_2)

def solution(str_1, str_2):
    chart_dirt = {}
    
    for c in str_1:
        if chart_dirt.has_key(c):
            chart_dirt[c] += 1
        else:
            chart_dirt[c] = 1

    for c in str_2:
        if chart_dirt.has_key(c):
            chart_dirt[c] -= 1
            if chart_dirt[c] < 0:
                return False
        else:
            return False
    
    return True

if __name__ == '__main__':
    main()
