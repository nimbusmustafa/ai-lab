from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QLabel
import math
import heapq

class Node:
    def __init__(self, name):
        self.name = name
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
    def __init__(self, rows, cols):
        self.nodes = {}
        self.rows = rows
        self.cols = cols

        for row in range(rows):
            for col in range(cols):
                name = f"{row},{col}"
                self.nodes[name] = Node(name)

        for row in range(rows):
            for col in range(cols):
                name = f"{row},{col}"
                current_node = self.nodes[name]
                if(row-1!=-1):
                    neighbor_name = f"{row-1},{col}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, 1)  
                    current_node.add_neighbor(neighbor_name, 1)
                if(col-1!=-1):   
                    neighbor_name = f"{row},{col-1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, 1)  
                    current_node.add_neighbor(neighbor_name, 1)
                if(row+1!=rows):
                    neighbor_name = f"{row+1},{col}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, 1)  
                    current_node.add_neighbor(neighbor_name, 1)
                if(col+1!=cols):   
                    neighbor_name = f"{row},{col+1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, 1)  
                if(col-1!=-1 and row-1 !=-1):
                    neighbor_name = f"{row-1},{col-1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, math.sqrt(2)) 
                if(col+1!=cols and row+1 !=rows):

                    neighbor_name = f"{row+1},{col+1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, math.sqrt(2))  # Horizontal neighbor
                if(col+1!=cols and row-1 !=-1):

                    neighbor_name = f"{row-1},{col+1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, math.sqrt(2))  # Horizontal neighbor
                if(col-1!=-1 and row+1 !=rows):
                    
                    neighbor_name = f"{row+1},{col-1}"
                    neighbor_node = self.nodes[neighbor_name]
                    current_node.add_neighbor(neighbor_name, math.sqrt(2))  # Horizontal neighbor
                # if row > 0:
                #     neighbor_name = f"{row-1},{col}"
                #     neighbor_node = self.nodes[neighbor_name]
                #     current_node.add_neighbor(neighbor_name, 1)  # Horizontal neighbor
                #     current_node.add_neighbor(neighbor_name, 1)  # Vertical neighbor
                # if col > 0:
                #     neighbor_name = f"{row},{col-1}"
                #     neighbor_node = self.nodes[neighbor_name]
                #     current_node.add_neighbor(neighbor_name, 1)  # Horizontal neighbor
                #     current_node.add_neighbor(neighbor_name, 1)  # Vertical neighbor
                # if row > 0 and col > 0:
                #     neighbor_name = f"{row-1},{col-1}"
                #     neighbor_node = self.nodes[neighbor_name]
                #     current_node.add_neighbor(neighbor_name, math.sqrt(2))  # Diagonal neighbor
                # if row > 0 and col < cols - 1:
                #     neighbor_name = f"{row-1},{col+1}"
                #     neighbor_node = self.nodes[neighbor_name]
                #     current_node.add_neighbor(neighbor_name, math.sqrt(2))  # Diagonal neighbor
                # if row == 0 and col == 0:
                #     neighbor_names=(f"{row+1},{col+1}" , f"{row},{col+1}",f"{row+1},{col}")
                #     for neighbor_name in neighbor_names:
                            
                #             if neighbor_name==f"{row+1},{col+1}":
                #              current_node.add_neighbor(neighbor_name, math.sqrt(2)) 
                #             else :
                #                 current_node.add_neighbor(neighbor_name, 1) 



        # for name, node in self.nodes.items():
        #     print(f"Node name: {name}")
        #     print(f"Neighbors:")
        #     for neighbor_name, weight in node.neighbors.items():
        #         print(f"  {neighbor_name}: {weight}")
        #     print(f"Visited: {node.visited}")
        #     print(f"g: {node.g}, h: {node.h}, f: {node.f}")
        #     print(f"Previous: {node.previous}")    
            
    def add_obstacle(self, node_name):
            if node_name in self.nodes:
                del self.nodes[node_name]
    def add_traffic(self, selected_locations):
     for location in selected_locations:
            row, col = location
            node_name = f"{row},{col}"
            current_node = self.nodes[node_name]


            for neighbor_name in current_node.neighbors:
                neighbor_row, neighbor_col = map(int, neighbor_name.split(','))

                if (neighbor_row, neighbor_col) in selected_locations:
                    # print(f"neighbour={neighbor_name}")

                    neighbor_node = self.nodes.get(neighbor_name)
                    if neighbor_node:
                       
                      current_node.add_neighbor(neighbor_name, 2 * current_node.neighbors[neighbor_name]) 
                    #   neighbor_node.add_neighbor(node_name, 2 * current_node.neighbors[neighbor_name])

            # selected_locations.append(location)
            # print(selected_locations)

    #  for name, node in self.nodes.items():
    #         print(f"Node name: {name}")
    #         print(f"Neighbors:")
    #         for neighbor_name, weight in node.neighbors.items():
    #             print(f"  {neighbor_name}: {weight}")
    #         print(f"Visited: {node.visited}")
    #         print(f"g: {node.g}, h: {node.h}, f: {node.f}")
    #         print(f"Previous: {node.previous}")              
    def add_highway(self, selected_locations):
     for location in selected_locations:
            row, col = location
            node_name = f"{row},{col}"
            current_node = self.nodes[node_name]


            for neighbor_name in current_node.neighbors:
                neighbor_row, neighbor_col = map(int, neighbor_name.split(','))

                if (neighbor_row, neighbor_col) in selected_locations:
                    # print(f"neighbour={neighbor_name}")

                    neighbor_node = self.nodes.get(neighbor_name)
                    if neighbor_node:
                       
                      current_node.add_neighbor(neighbor_name, 0.5 * current_node.neighbors[neighbor_name]) 
     for name, node in self.nodes.items():
      print(f"Node name: {name}")
      print(f"Neighbors:")
     for neighbor_name, weight in node.neighbors.items():
        print(f"  {neighbor_name}: {weight}")
        print(f"Visited: {node.visited}")
        print(f"g: {node.g}, h: {node.h}, f: {node.f}")
        print(f"Previous: {node.previous}")                  


    def heuristic(self, row1, col1, row2, col2):
        maths= math.sqrt((row1 - row2)**2 + (col1 - col2)**2)
        return maths

    def a_star(self, start_name, end_name):
        start_node = self.nodes[start_name]
        end_node = self.nodes[end_name]
        print(end_node)

        start_node.g = 0
        start_node.h = self.heuristic(*map(int, start_name.split(',')), *map(int, end_name.split(',')))
        start_node.f = start_node.g + start_node.h

        open_set = [(start_node.f, start_node)]
        heapq.heapify(open_set)

        all_paths = []

        while open_set:
            current = heapq.heappop(open_set)[1]

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
                    print(neighbor,weight)

            for neighbor, weight in current.neighbors.items():
                if neighbor in self.nodes.keys() and not self.nodes[neighbor].visited :

                    temp_g = current.g + weight
                    if temp_g <= self.nodes[neighbor].g:
                        self.nodes[neighbor].previous = current
                        self.nodes[neighbor].g = temp_g
                        self.nodes[neighbor].h = self.heuristic(*map(int, neighbor.split(',')), *map(int, end_name.split(',')))
                        self.nodes[neighbor].f = self.nodes[neighbor].g + self.nodes[neighbor].h
                        heapq.heappush(open_set, (self.nodes[neighbor].f, self.nodes[neighbor]))

        return all_paths


class GridWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Selection")
        self.setGeometry(100, 100, 800, 600)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.selected_locations = set()
        self.obstacle_locations = set()
        self.traffic_locations = []
        self.highway_locations=[]

        self.current_destination = None
        self.final_destination = None
        self.graph = Graph(10,10)

        self.create_grid_buttons()
        self.create_add_obstacle_button()
        self.create_select_current_destination_button()
        self.create_select_final_destination_button()
        self.create_traverse_button()
        self.create_select_traffic_button()
        self.create_select_highway_button()
        self.create_cost_label()  

    def create_grid_buttons(self):
        for row in range(10):
            for col in range(10):
                button = QPushButton()
                button.clicked.connect(lambda state, row=row, col=col: self.grid_button_clicked(row, col))
                self.grid_layout.addWidget(button, row, col)
    def create_select_highway_button(self):
        select_highway_button = QPushButton("Select Highway")
        select_highway_button.clicked.connect(self.highway_button_clicked)
        self.grid_layout.addWidget(select_highway_button, 10, 0, 1, 5)

    def create_add_obstacle_button(self):
        add_obstacle_button = QPushButton("Add Obstacle")
        add_obstacle_button.clicked.connect(self.add_obstacle_button_clicked)
        self.grid_layout.addWidget(add_obstacle_button, 10, 5, 1, 5)

    def create_select_current_destination_button(self):
        select_current_destination_button = QPushButton("Select Current Destination")
        select_current_destination_button.clicked.connect(self.select_current_destination_button_clicked)
        self.grid_layout.addWidget(select_current_destination_button, 12, 0, 1, 5)

    def create_select_final_destination_button(self):
        select_final_destination_button = QPushButton("Select Final Destination")
        select_final_destination_button.clicked.connect(self.select_final_destination_button_clicked)
        self.grid_layout.addWidget(select_final_destination_button, 12, 5, 1, 5)

    def create_traverse_button(self):
        traverse_button = QPushButton("Traverse")
        traverse_button.clicked.connect(self.traverse_button_clicked)
        self.grid_layout.addWidget(traverse_button, 14, 0, 1, 5)

    def create_select_traffic_button(self):
        select_traffic_button = QPushButton("Select Traffic")
        select_traffic_button.clicked.connect(self.traffic_button_clicked)
        self.grid_layout.addWidget(select_traffic_button, 14, 5, 1, 5)

    def highway_button_clicked(self):
        if not self.selected_locations:
            QMessageBox.warning(self, "Warning", "Please select grid locations first.")
            return
        for location in self.selected_locations:
            row,col =location
            button = self.grid_layout.itemAtPosition(row,col).widget()
            button.setStyleSheet("background-color: blue; color: white;")
        self.highway_locations.extend(self.selected_locations)
        print("Highway locations added:", self.highway_locations)

        self.graph.add_highway(self.highway_locations)
        self.selected_locations.clear()

    def traffic_button_clicked(self):
        if not self.selected_locations:
            QMessageBox.warning(self, "Warning", "Please select grid locations first.")
            return
        for location in self.selected_locations:
            row,col =location
            button = self.grid_layout.itemAtPosition(row,col).widget()
            button.setStyleSheet("background-color: red; color: white;")
        self.traffic_locations.extend(self.selected_locations)
        print("Traffic locations added:", self.traffic_locations)

        self.graph.add_traffic(self.traffic_locations)

        # print("Traffic locations added:", self.traffic_locations)
        self.selected_locations.clear()



    def grid_button_clicked(self, row, col):
        location = (row, col)
        if location in self.selected_locations:
            self.selected_locations.remove(location)
            print(f"Location deselected: {location}")
        else:
            self.selected_locations.add(location)
            print(f"Location selected: {location}")

    def add_obstacle_button_clicked(self):
        if not self.selected_locations:
            QMessageBox.warning(self, "Warning", "Please select a grid location first.")
            return

        for location in self.selected_locations:
            self.obstacle_locations.add(location)
            print(f"Location added as obstacle: {location}")
            row,col=location
            self.graph.add_obstacle(f"{row},{col}")

            button = self.grid_layout.itemAtPosition(location[0], location[1]).widget()
            button.setStyleSheet("background-color: black; color: white;")  

        self.selected_locations.clear()
        print("Obstacles added.")
    def create_cost_label(self):
        self.cost_label = QLabel()
        self.grid_layout.addWidget(self.cost_label, 16, 0, 1, 5)  # Span the label across the entire grid

    def select_current_destination_button_clicked(self):
        if not self.selected_locations:
            QMessageBox.warning(self, "Warning", "Please select one grid location as the current destination.")
            return

        self.current_destination = next(iter(self.selected_locations))
        print(f"Current destination selected: {self.current_destination}")

        button = self.grid_layout.itemAtPosition(self.current_destination[0], self.current_destination[1]).widget()
        button.setStyleSheet("background-color: grey; color: white;")  
        self.selected_locations.clear()

    def select_final_destination_button_clicked(self):
        if not self.selected_locations:
            QMessageBox.warning(self, "Warning", "Please select one grid location as the final destination.")
            return

        self.final_destination = next(iter(self.selected_locations))
        print(f"Final destination selected: {self.final_destination}")

        button = self.grid_layout.itemAtPosition(self.final_destination[0], self.final_destination[1]).widget()
        button.setStyleSheet("background-color: grey; color: white;")  
        self.selected_locations.clear()

    def traverse_button_clicked(self):
        if not self.current_destination or not self.final_destination:
            QMessageBox.warning(self, "Warning", "Please select the current and final destinations.")
            return

        start_name = f"{self.current_destination[0]},{self.current_destination[1]}"
        end_name = f"{self.final_destination[0]},{self.final_destination[1]}"
        shortest_paths = self.graph.a_star(start_name, end_name)
        if shortest_paths:
            for path, total_cost in shortest_paths:
                print(f"Path: {' -> '.join(path)}")
                print(f"Total cost: {total_cost}")
                self.cost_label.setText(f"Total cost: {total_cost}")  

                for node_name in path:
                 row, col = map(int, node_name.split(','))
                 button = self.grid_layout.itemAtPosition(row, col).widget()
                 button.setStyleSheet("background-color: yellow; color: black;") 
        else:
            print("No paths found!")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec_())
