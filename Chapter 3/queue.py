class Queue(object):
    def __init__(self):
        self.list = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def add(self, val):
        self.list.append(val)
        self.size += 1

    def remove(self):
        del self.list[0]
        self.size -= 1

    def front(self):
        return self.list[0]
