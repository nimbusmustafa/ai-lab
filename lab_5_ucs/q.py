class Graph:
    def __init__(self, graph_dict=None):
        self.graph = graph_dict if graph_dict else {}


    def uniform_cost_search(self, start, goal):
        visited = []
        priority_queue = [(0, start, [])]

        while priority_queue:
            priority_queue.sort(key=lambda x: x[0])
            current_cost, current_node, path = priority_queue.pop(0)

            if current_node in visited:
                continue
            if current_node == goal and len(path) > 1:
             return path, current_cost
            visited.append(current_node)
            path = path + [current_node]

            if current_node == goal:
                return path, current_cost

            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    priority_queue.append((current_cost + edge_cost, neighbor, path))

        return None

if __name__ == '__main__':
    graph_dict = {
        'S': [('A', 5), ('B', 9),('D', 6)],
        'B': [('A', 2), ('C', 1)],
        'D': [('C', 2),('E',2)],
        'C': [('G2', 5),('F',7),('S',6)],
        'A': [('B',3),('G1',9)],
        'E': [('G3', 7)],
        'F': [('G3', 8),('D',2)],
        'G1':[],
        'G2':[],
        'G3':[]
    }

    g = Graph(graph_dict)

    start_node = 'S'
    goal_node = ['G1','G2','G3']

    for goal_nodess in goal_node:
     result = g.uniform_cost_search(start_node, goal_nodess)

     if result:
        path, cost = result
        print(f"Optimal Path: {path}")
        print(f"Optimal Cost: {cost}")
     else:
        print(f"No path found from {start_node} to {goal_node}")
