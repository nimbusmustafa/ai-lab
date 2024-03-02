class Graph:
    def __init__(self, edges, n):
        self.adj_list = [] 
        for x in range(n): 
            self.adj_list.append([]) 
        for (src, dest, weight) in edges:
            self.adj_list[src].append((dest, weight))

def printGraph(graph):
    for src in range(len(graph.adj_list)):
        for dest,weight in graph.adj_list[src]:
            print(f'({src} -> {dest} , {weight}) ', end='')
        print()

if __name__ == '__main__':
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))

    edges = []
    for _ in range(m):
        src = int(input("Enter the source vertex: "))
        dest = int(input("Enter the destination vertex: "))
        weight=int(input("Enter the weights: "))
        edges.append((src, dest, weight))

    graph = Graph(edges, n)
    print("Adjacency List:")
    printGraph(graph)
