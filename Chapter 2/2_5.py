from linked_list import LinkedList

def main():
    l_1 = LinkedList()
    l_2 = LinkedList()

    l_1.add_node_tail(7)
    l_1.add_node_tail(1)
    l_1.add_node_tail(6)

    l_2.add_node_tail(5)
    l_2.add_node_tail(9)
    l_2.add_node_tail(2)

    l_1.print_list(), l_2.print_list()
    
    answer = solution_1(l_1, l_2)
    answer.print_list()

    l_3 = LinkedList()
    l_4 = LinkedList()

    l_3.add_node_tail(6)
    l_3.add_node_tail(1)
    l_3.add_node_tail(7)

    l_4.add_node_tail(2)
    l_4.add_node_tail(9)
    l_4.add_node_tail(5)

    l_3.print_list(), l_4.print_list()
    
    answer = solution_2(l_3, l_4)
    answer.print_list()

def solution_1(l_1, l_2):
    digit_1 = l_1.head.next
    digit_2 = l_2.head.next
    
    answer_l = LinkedList()
    ten = False

    while digit_1.next != None:
        val = digit_1.data + digit_2.data
        
        if ten == True:
            val += 1
            ten = False
        
        if val >= 10:
            temp = str(val)
            val = int(temp[1]) 
            ten = True

        answer_l.add_node_tail(val)

        digit_1 = digit_1.next
        digit_2 = digit_2.next

    return answer_l

def solution_2(l_1, l_2):
    digit_1 = l_1.tail.prev
    digit_2 = l_2.tail.prev
    
    answer_l = LinkedList()
    ten = False

    while digit_1.prev != None:
        val = digit_1.data + digit_2.data
        if ten == True:
            val += 1
            ten = False
        
        if val >= 10:
            temp = str(val)
            val = int(temp[1]) 
            ten = True
        
        answer_l.add_node_head(val)

        digit_1 = digit_1.prev
        digit_2 = digit_2.prev

    return answer_l

if __name__== '__main__':
    main()    
