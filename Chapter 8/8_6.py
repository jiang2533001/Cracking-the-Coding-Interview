from stack import Stack

def main():
    stack_sets = []
    for i in range(3):
        stack_sets.append(Stack())
    
    n = 3
    items = range(n, 0, -1)

    map(stack_sets[0].push, items)
    print_game(stack_sets)

    solution(stack_sets)
    print_game(stack_sets)

def solution(stack_sets):
    

def print_game(stack_sets):
    for i in range(3):
        stack_sets[i].print_stack()



if __name__ == '__main__':
    main()
