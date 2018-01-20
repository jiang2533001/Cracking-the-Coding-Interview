from stack import Stack

def main():
    stack = Stack() 
    items = [2, 3, 8, 9, 1, 4, 5, 7, 6]

    map(stack.push, items)
    stack.print_stack()

    solution(stack)
    stack.print_stack()

def solution(stack):
    temporary = Stack()
    temporary.push(stack.pop())

    while not stack.is_empty():
        compare = stack.pop()
        while compare < temporary.front() and (not temporary.is_empty()):
            stack.push(temporary.pop())
        
        temporary.push(compare)
    
    while not temporary.is_empty():
        stack.push(temporary.pop())

if __name__=='__main__':
    main()
