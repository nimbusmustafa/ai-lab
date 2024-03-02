class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vert(self, name):
        if name in self.graph_dict:
            print("Vertex", name, "already exists")
        self.graph_dict[name] = []

    def add_edge(self, vert, dest, weight):
        if vert not in self.graph_dict or dest not in self.graph_dict:
            print("Invalid edge")
        else:
            self.graph_dict[vert].append([dest, weight])

    def adjacency_list(self):
        print(self.graph_dict)

    def adjacency_matrix(self):
        mat = []
        for i in self.graph_dict:
            m = [0] * len(self.graph_dict)

            for rhs in self.graph_dict[i]:
                m[rhs[0] - 1] = rhs[1]
            mat.append(m)
        print(mat)

def main():
    g = Graph()

    while True:
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Show Adjacency List")
        print("4. Show Adjacency Matrix")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = int(input("Enter vertex name: "))
            g.add_vert(name)
        elif choice == 2:
            vert = int(input("Enter source vertex: "))
            dest = int(input("Enter destination vertex: "))
            weight = int(input("Enter weight: "))
            g.add_edge(vert, dest, weight)
        elif choice == 3:
            g.adjacency_list()
        elif choice == 4:
            g.adjacency_matrix()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
