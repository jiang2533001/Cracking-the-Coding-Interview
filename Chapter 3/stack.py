class Stack(object):
    def __init__(self):
        self.head = None
        self.list = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, val):
        self.list.append(val)
        self.head = self.size
        self.size += 1

    def pop(self):
        if not self.is_empty():
            val = self.list[self.head]
            del self.list[self.head]
            self.size -= 1
            self.head = self.size - 1 
            return val

    def front(self):
        return self.list[self.head]

    def print_stack(self):
        print '[',
        for i in range(self.size-1, -1, -1):
            print self.list[i],
        print ']'
