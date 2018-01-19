from linked_list import LinkedList
from stack import Stack

def main():
    l_l = LinkedList()
    items = ['a', 'b', 'c']
    map(l_l.add_node_tail, items)
    map(l_l.add_node_head, items)

    l_l.print_list()
    print solution(l_l)

def solution(l_l):
    faster_runner = l_l.head.next.next
    slower_runner = l_l.head.next
    stack = Stack()

    while faster_runner.next.next != None:
        stack.push(slower_runner.data)
        slower_runner = slower_runner.next
        faster_runner = faster_runner.next.next
   
    stack.push(slower_runner.next.data)
    test_node = slower_runner.next

    while not stack.is_empty():        
        if stack.pop() != test_node.data:
            return False
        else:
            test_node = test_node.next
        
    return True

if __name__ == '__main__':
    main()
