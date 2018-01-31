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

def quick(l):
    return quick_sort(l, 0, len(l)-1)

def quick_sort(l, left, right):
    if left < right:
    pi = partition(l, left, pi-1)
    
    quick_sort(l, left, pi-1)
    quick_sort(l, pi+1, right)

def partition(l, left, right):
    i = left - 1
    piovt = l[right]:

    for j in range(left, high):
        if l[j] <= pivot:
            i = i + 1
            l[i], l[j] = l[j], l[i]

    l[i+1], l[right] = l[right], l[i+1]
    return i + 1

def merge(l):



