class Node(object):
    def __init__(self, val, p, n):
        self.data = val
        self.prev = p
        self.next = n

class LinkedList(object):
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def add_node_head(self, val):
        node = Node(val, self.head, self.head.next)
        self.head.next = node
        node.next.prev = node
        self.size += 1

    def add_node_tail(self, val):
        node = Node(val, self.tail.prev, self.tail)
        self.tail.prev = node
        node.prev.next = node
        self.size += 1

    def delete(self, index):
        if self.is_empty():
            print 'The linked list is empty!'
        else:
            if index > self.size:
                print 'The index is out of range of linked list!'
            else:    
                current = self.head
                for i in range(index):
                    current = current.next 
                
                current.next.prev = current.prev
                current.prev.next = current.next
                del current
                self.size -= 1
    
    def contain_element(self, val):
        if self.is_empty():
            print 'The linked list is empty!'
        else:
            current = self.head.next
            for i in range(self.size):
                if current.data == val:
                    return True
                
                current = current.next
            return False

    def print_list(self):
        if self.is_empty():
            print 'The linked list is empty!'
        else:
            current = self.head.next
            for i in range(self.size-1):
                print str(current.data) + ' ->',
                current = current.next

            print current.data
