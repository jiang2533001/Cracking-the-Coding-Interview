from linked_list import LinkedList
def main():
    l_l = LinkedList()
    items = range(1, 10)
    map(l_l.add_node_tail, items)
    
    solution(l_l)
    l_l.print_list()

def solution(l_l):
    pointer_1 = l_l.head
    pointer_2 = l_l.tail
    
    while pointer_1 != pointer_2 or pointer_1 != pointer_2.prev:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.prev
        
    l_l.delete_node(pointer_1)

if __name__ == '__main__':
    main()
