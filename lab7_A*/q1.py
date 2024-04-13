class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 5,
            'B': 6,
            'C': 5,
            'D': 15,
            'X':5,
            'Y':8,
            'E':0


        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = [start_node]
        closed_list = []

        g = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            n = open_list.pop(0)  
            for v in open_list:
                if g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found:', reconst_path)
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.append(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.append(m)

            closed_list.append(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'S': [('A', 1), ('B', 2)],
    'B': [('S', 2), ('C', 7), ('D', 1)],
    'A': [('S', 1), ('X', 4), ('Y', 7)],
    'C': [('B', 7), ('E', 5)],
    'D': [('B', 1), ('E', 12)],
    'X': [('A', 4), ('E', 2)],
    'Y': [('A', 7), ('E', 3)],
    'E': [('X', 2), ('Y', 3), ('C', 5), ('D', 12)],
}
graph = Graph(adjacency_list)
graph.a_star_algorithm('S', 'E')
