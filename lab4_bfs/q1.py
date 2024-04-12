class Graph:
    def __init__(self):
        self.graph = {
        '0': [],
        '1': [],
        '2': ['3'],
        '3': ['1'],
        '4': ['1', '0'],
        '5': ['0', '2']
        }

    def topological_sort_bfs(self):
        in_degree = {}
        for node, _ in self.graph.items():
            in_degree[node] = 0

        for neighbors in self.graph.values():
            for node in neighbors:
                in_degree[node] += 1

        queue = []
        for node, degree in in_degree.items():
            if degree == 0:
                # print(node)
                queue.append(node)
        result = []

        while queue:
            current_node = queue.pop(0)
            # print(current_node)
            result.append(current_node)

            for neighbor in self.graph[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)


        return result

if __name__ == "__main__":
    g = Graph()

    topological_order = g.topological_sort_bfs()

    if topological_order:
        print("Topological Order:", topological_order)
