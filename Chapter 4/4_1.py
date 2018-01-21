from graph import Graph, Node
from stack import Stack
from queue import Queue

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

    print DFS(graph.vertices_set[3], graph.vertices_set[0])
    print BFS(graph.vertices_set[3], graph.vertices_set[0])

def DFS(start, end):
    stack = Stack()    
    stack.push(start)
    
    visited_set = {}
    visited_set[start.label] = True

    while not stack.is_empty():
        current = stack.pop()
        for i in range(current.neighbors_num):
            node = current.neighbors[i]
            if not visited_set.has_key(node.label):
                visited_set[node.label] = True
                if node.label == end.label:
                    return True
                else:
                    stack.push(node)
    return False

def BFS(start, end):
    queue = Queue()
    queue.add(start)

    visited_set = {}
    visited_set[start.label] = True

    while not queue.is_empty():
        current = queue.remove()
        for i in range(current.neighbors_num):
            node = current.neighbors[i]
            if not visited_set.has_key(node.label):
                visited_set[node.label] = True
                if node.label == end.label:
                    return True
                else:
                    queue.add(node)
    return False

if __name__ == '__main__':
    main()
