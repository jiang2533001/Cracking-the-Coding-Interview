from stack import Stack

class MyQueue(object):
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def is_empty(self):
        if self.stack_1.is_empty():
            return True
        else:
            return False

    def add(self, val):
        self.stack_1.push(val)

    def remove(self):
        if not self.is_empty():
            self.shift_to_2()
            result = self.stack_2.pop()
            self.shift_to_1()
            return result

    def front(self):
        if not self.is_empty():
            self.shift_to_2()
            result = self.stack_2.front()
            self.shift_to_1()
            return result
        
    def shift_to_2(self):
        for i in range(self.stack_1.size):
            val = self.stack_1.pop()
            self.stack_2.push(val)

    def shift_to_1(self):
        for i in range(self.stack_2.size):
            val = self.stack_2.pop()
            self.stack_1.push(val)

    def print_queue(self):
        self.shift_to_2()
        self.stack_2.print_stack()
        self.shift_to_1()

def main():
    myqueue = MyQueue()
    items = [1, 2, 3, 4, 5]

    map(myqueue.add, items)
    myqueue.print_queue()

    myqueue.remove()
    myqueue.print_queue()

    print myqueue.front()

if __name__=='__main__':
    main()
