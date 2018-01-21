class Node(object):
    def __init__(self, label, neighbor=None)
        self.label = label
        if neighbor!=None:
            self.neighbors = [neighbor]
            self.neighbors_num = 1
        else:
            self.neighbors = []
            self.neighbors_num = 0

    def add_neigbor(self, node)
        self.neighbors.append(node)
        self.neighbors_num += 1

class Graph(object):
    def __init__(self):
        self.edges_num = 0
        self.vertices_num = 0
        self.vertex_set = []

    def add_vertex(self, label):
        node = Node(label)
        self.vertex_set.append(node)
        self.vertices += 1

    def connect_vertices(self, node_1, node_2, directed=True):
        node_1.add_neighbor(node_2)
        self.edges_num += 1

        if not directed:
            node_2.add_neighbor(node_1)

    def print_matrix(self):
        matrix = [[0]*self.vertices_num]*self.vertices
        
        for i in range(self.vertices_num):
            node = self.vertices_set[i]
            for j in range(node.neigbors_num):
                matrix[i][node.neighbors[j]] = 1

        for i in range(self.vertices_num):
            for j in range(self.vertices_num):
                print matrix[i][j]
            print '\n'
