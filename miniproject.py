import heapq
import math

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = {}
        self.visited = False
        self.g = math.inf
        self.h = 0
        self.f = math.inf
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def __lt__(self, other):
        return self.f < other.f    

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, start, end, weight):
        self.nodes[start].add_neighbor(self.nodes[end], weight)
        self.nodes[end].add_neighbor(self.nodes[start], weight)

    def add_obstacle(self, node_name):
        if node_name in self.nodes:
            del self.nodes[node_name]

    def heuristic(self, node1, node2):
        return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

    def a_star(self, start_name, end_name):
        start_node = self.nodes[start_name]
        end_node = self.nodes[end_name]
        start_node.g = 0
        start_node.h = self.heuristic(start_node, end_node)
        start_node.f = start_node.g + start_node.h

        open_set = [(start_node.f, start_node)]
        heapq.heapify(open_set)
        all_paths = []

        while open_set:
            current = heapq.heappop(open_set)[1]
            if current is None:
                        break
            if current == end_node:
                path = []
                total_cost = current.g  
                while current:
                    path.append(current.name)
                    current = current.previous
                all_paths.append((path[::-1], total_cost))
                continue

            current.visited = True

            for neighbor, weight in current.neighbors.items():
                if neighbor.name in self.nodes and not neighbor.visited:
                    temp_g = current.g + weight
                    if temp_g < neighbor.g:
                        neighbor.previous = current
                        neighbor.g = temp_g
                        neighbor.h = self.heuristic(neighbor, end_node)
                        neighbor.f = neighbor.g + neighbor.h
                        heapq.heappush(open_set, (neighbor.f, neighbor))

        return all_paths

def build_city_graph():
    graph = Graph()
    locations = {
        "A": (0, 0),
        "B": (0, 1),
        "C": (0, 2),
        "D": (0, 3),
        "E": (1, 0),
        "F": (1, 1),
        "G": (1, 2),
        "H": (1, 3),
        "I": (2, 0),
        "J": (2, 1),
        "K": (2, 2),
        "L": (2, 3),
        "M": (3, 0),
        "N": (3, 1),
        "O": (3, 2),
        "P": (3, 3)
    }
    for name, (x, y) in locations.items():
        graph.add_node(Node(name, x, y))

    edges = [
        ("A", "B", 1),
        ("B", "C", 1),
        ("C", "D", 1),
        ("E", "F", 1),
        ("F", "G", 1),
        ("G", "H", 1),
        ("I", "J", 1),
        ("J", "K", 1),
        ("K", "L", 1),
        ("M", "N", 1),
        ("N", "O", 1),
        ("O", "P", 1),
        ("A", "E", 1),
        ("B", "F", 1),
        ("C", "G", 1),
        ("D", "H", 1),
        ("E", "I", 1),
        ("F", "J", 1),
        ("G", "K", 1),
        ("H", "L", 1),
        ("I", "M", 1),
        ("J", "N", 1),
        ("K", "O", 1),
        ("L", "P", 1),
        ("A", "F", math.sqrt(2)),
        ("B", "E", math.sqrt(2)),
        ("B", "G", math.sqrt(2)),
        ("C", "F", math.sqrt(2)),
        ("C", "H", math.sqrt(2)),
        ("D", "G", math.sqrt(2)),
        ("E", "J", math.sqrt(2)),
        ("F", "I", math.sqrt(2)),
        ("F", "K", math.sqrt(2)),
        ("G", "J", math.sqrt(2)),
        ("G", "L", math.sqrt(2)),
        ("H", "K", math.sqrt(2)),
        ("I", "N", math.sqrt(2)),
        ("J", "M", math.sqrt(2)),
        ("J", "O", math.sqrt(2)),
        ("K", "N", math.sqrt(2)),
        ("K", "P", math.sqrt(2)),
        ("L", "O", math.sqrt(2)),
        ("M", "J", math.sqrt(2)),
        ("N", "I", math.sqrt(2)),
        ("N", "K", math.sqrt(2)),
        ("O", "J", math.sqrt(2)),
        ("O", "L", math.sqrt(2)),
        ("P", "K", math.sqrt(2))
    ]
    for start, end, weight in edges:
        graph.add_edge(start, end, weight)

    obstacles = ["M", "L"]
    for obstacle in obstacles:
        graph.add_obstacle(obstacle)

    traffic_edges = [
        ("A", "B", 2), ("A", "E", 2), ("B", "C", 2)
    ]


    for start, end, weight in traffic_edges:
        graph.add_edge(start, end, weight)

    highway_edges = [
        ("G", "K", 0.5), ("K", "O", 0.5)
    ]
    for start, end, weight in highway_edges:
        graph.add_edge(start, end, weight)  

    return graph

def main():
    graph = build_city_graph()

    while True:
        print("Available destinations:")
        for node_name in graph.nodes:
            print(f"- {node_name}")

        start = input("Enter your current location: ").upper()
        if start not in graph.nodes:
            print("Invalid location. Please try again.")
            continue

       
        end = input("Enter your destination: ").upper()
        if end not in graph.nodes:
            print("Invalid destination. Please try again.")
            continue

        shortest_paths = graph.a_star(start, end)
        if shortest_paths:
            for path, total_cost in shortest_paths:
                print(f"Path: {' -> '.join(path)}")
                print(f"Total cost: {total_cost}")
        else:
            print("No paths found!")
        for node in graph.nodes.values():
            node.visited = False
            node.g = math.inf
            node.f = math.inf
            node.previous = None
            
        choice = input("Do you want to find another route? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()