from stack import Stack

class SetOfStacks(object):
    def __init__(self):
        self.list_of_stack = []
        stack = Stack()
        self.list_of_stack.append(stack)
        self.size = 1

    def push(self, val):
        last_stack = self.list_of_stack[self.size-1]
        if last_stack.size < 3:
            last_stack.push(val)
        else:
            new_stack = Stack()
            new_stack.push(val)
            self.list_of_stack.append(new_stack)
            self.size += 1

    def pop(self):
        last_stack = self.list_of_stack[self.size-1]
        result = last_stack.pop()
        if last_stack.size == 0:
            del self.list_of_stack[self.size-1]
            self.size -= 1
        
        return result
    
    def print_list_stack(self):
        for i in range(self.size):
            stack = self.list_of_stack[i]
            stack.print_stack()


def main():
    s_o_s = SetOfStacks()
    items = [1, 2, 3, 4, 5, 6, 7]
    map(s_o_s.push, items)

    s_o_s.print_list_stack()
    print s_o_s.pop()
    s_o_s.print_list_stack()

if __name__ == '__main__':
    main()

