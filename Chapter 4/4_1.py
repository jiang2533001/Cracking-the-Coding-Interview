from graph import Graph, Node

def main():
    graph = Graph()
    map(graph.add_vertex, range(6))

    graph.connect_vertices(graph.vertices_set[0], graph.vertices_set[1])
    graph.connect_vertices(graph.vertices_set[0], graph.vertices_set[4])
    graph.connect_vertices(graph.vertices_set[1], graph.vertices_set[3])
    graph.connect_vertices(graph.vertices_set[1], graph.vertices_set[4])
    graph.connect_vertices(graph.vertices_set[2], graph.vertices_set[1])
    graph.connect_vertices(graph.vertices_set[3], graph.vertices_set[2])
    graph.connect_vertices(graph.vertices_set[3], graph.vertices_set[4])
    graph.connect_vertices(graph.vertices_set[0], graph.vertices_set[5])

    print DFS()
    print BFS()

def DFS():


def BFS():


if __name__ == '__main__':
    main()
