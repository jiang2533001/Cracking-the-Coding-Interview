from linked_list import LinkedList

def main():
    l_l = LinkedList()
    items = [1, 2, 3, 4, 4, 5, 2]
    map(l_l.add_node_tail, items)
    
    l_l.print_list()
    
    solution(l_l)
    l_l.print_list()

def solution(link_list):
    dirct = {}
    
    current = link_list.head.next
    while current.next != None:
        if dirct.has_key(current.data):
            link_list.delete_node(current)
        else:
            dirct[current.data] = True

        current = current.next

if __name__ == '__main__':
    main()
