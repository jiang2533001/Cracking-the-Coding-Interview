def bubble(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selection(l):
    for i in range(len(l)-1):
        jmin = i
        for j in range(i+1, len(l)):
            if a[j] < a[imin]:
                jmin = j

        if jmin != j:
            l[j], l[jmin] = l[jmin], l[j]
    
    return l

def insert(l):
    for i in range(1, len(l)):
            temp = l[i]
            for j in range(i-1, -1, -1):
                if l[j] > temp:
                    l[i], l[i+1] = l[i+1], l[i]
                else:
                    break
    return l

def merge(l):



