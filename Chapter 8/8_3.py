def main()：
    
    #arrary = [-40, -30, -1, 0, 1, 2, 4, 7, 9, 11, 21]
    array = [1, 3, 4, 5, 6]
    print solution(array, 0, len(array)-1)

def solution(array, start, end)
    if end < start:
        return False
    
    mid = (start + end) / 2
    if array[mid] == mid:
        return True
    elif:
        if array[mid] > mid:
            return solution(array, start, mid - 1)
    else:
        return solution(array, mid + 1, end)


if __name__ == '__main__':
    main()
