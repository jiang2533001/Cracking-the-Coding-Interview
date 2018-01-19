from linked_list import LinkedList

def main():
    l_l = LinkedList()
    new_l_l = LinkedList()

    items = range(1, 11)
    map(l_l.add_node_tail, items)
    l_l.print_list()

    k = 3
    
    node = solution_1(l_l, k)
    #node = solution_2(l_l.head, k)
    
    new_l_l.head.next = node
    node.prev = new_l_l.head
    new_l_l.print_list()
    
def solution_1(l_l, k):
    current = l_l.head.next
    index = 1
    found = False
    while current.next != None:
        if index == k:
            found = True
        
        if found == True:
            return current 
        
        current = current.next
        index += 1


def solution_2(node, k):
    if k == 0:
        return node
    else:
        return solution_2(node.next, k-1)


if __name__=='__main__':
    main()
