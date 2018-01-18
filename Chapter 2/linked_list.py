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

    def delete_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del node
        self.size -= 1
  
    def contain_element(self, val):
        current = self.head.next
        while current.next != None:
            if current.data == val:
                return True
                
            current = current.next
        return False

    def print_list(self):
        current = self.head.next
        while current.next.next != None:
            print str(current.data) + ' ->',
            current = current.next

        print current.data
