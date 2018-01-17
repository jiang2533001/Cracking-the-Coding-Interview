from linked_list import LinkedList

def main():
    l_l = LinkedList()
    
    l_l.add_node_tail(1)
    l_l.add_node_tail(2)
    l_l.add_node_tail(3)
    l_l.add_node_tail(4)
    l_l.add_node_tail(4)
    l_l.add_node_tail(5)
    l_l.add_node_tail(2)
    l_l.print_list()
    
    solution(l_l)
    l_l.print_list()

def solution(link_list):
    dirct = {}
    
    current = link_list.head.next
    while current != link_list.tail:
        if dirct.has_key(current.data):
            link_list.delete_node(current)
        else:
            dirct[current.data] = True

        current = current.next

if __name__ == '__main__':
    main()
