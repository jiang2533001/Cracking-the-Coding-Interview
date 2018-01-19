from linked_list import LinkedList

def main():
    l_l = LinkedList()
    items = [3, 5, 8, 5, 10, 2, 1]

    map(l_l.add_node_tail, items)
    
    before, after = solution(l_l, 5)
    before.print_list()
    after.print_list()
def solution(l_l, x):
    node = l_l.head.next
    before = LinkedList()
    after = LinkedList()

    while node.next != None:
        if node.data < 5:
            before.add_node_tail(node.data)
        else:
            after.add_node_tail(node.data)
        
        node = node.next

    return before, after


if __name__ == '__main__':
    main()
