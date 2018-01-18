from linked_list import LinkedList
def main():
    l_l = LinkedList()
    items = range(1, 11)
    map(l_l.add_node_tail, items)
    l_l.print_list() 
    
    solution(node)
    l_l.print_list()

def solution(l_l):
    pointer_1 = l_l.head
    pointer_2 = l_l.tail
    
    while pointer_1 != pointer_2 and pointer_1.next != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.prev
        
    l_l.delete_node(pointer_1)

if __name__ == '__main__':
    main()
