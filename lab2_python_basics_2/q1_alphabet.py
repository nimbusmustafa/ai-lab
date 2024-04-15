class Graph:
    def __init__(self, edges, vertices):
        self.adj_list = {}
        for vertex in vertices:
            self.adj_list[vertex] = []
        for (src, dest) in edges:
            self.adj_list[src].append(dest)

def printGraph(graph):
    for src, dest_list in graph.adj_list.items():
        for dest in dest_list:
            print(f'({src} -> {dest}) ', end='')
        print()

# if __name__ == '__main__':
vertices = input("Enter the vertices separated by commas (e.g., A,B,C): ").split(',')
n = len(vertices)
m = int(input("Enter the number of edges: "))

edges = []
for _ in range(m):
    src = input("Enter the source vertex: ")
    dest = input("Enter the destination vertex: ")
    edges.append((src, dest))

graph = Graph(edges, vertices)
print("Adjacency List:")
printGraph(graph)
