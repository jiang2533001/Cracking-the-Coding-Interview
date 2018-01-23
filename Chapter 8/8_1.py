def main():
    n = 100 
    print solution(n)

def solution(n):
    step = [1, 2, 3]
    Min = [0]

    for i in range(1, n+1):
        Min.append(find_min(i, Min, step))  
   
    return Min[n]

def find_min(i, Min, step):
    num_list = []
    for num in step:
        if i>=num:
            num_list.append(Min[i-num]+1)
    
    return min(num_list)

if __name__ == '__main__':
    main()
