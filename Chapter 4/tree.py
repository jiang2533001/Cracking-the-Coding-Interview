class Node(object):
    def __init__(self, val)
    self.val = val
    self.left = None
    self.right = None

class Binary_Tree(object):
    def __init__(self, val)
        self.root = Node(val)


    def add_node(self, val)


    def remove_node(self, val)


    def search(self, node, val):
        if node.val == val:
            return True
        if node.right == None and node.left == None 
            return False
        else:
            if node.val <= val:
                return self.search(node.right, val)
            else:
                return self.search(node.left, val)
            
    def print_node(val)
