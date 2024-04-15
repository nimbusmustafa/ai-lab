class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def generate_children(self):
        children = []
        zero_row, zero_col = self.find_blank()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                child = Node(new_state, self, move)
                children.append(child)
        return children

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j


class PuzzleSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def misplaced_tiles_heuristic(self, state):
        sum=0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    sum+=1

        return sum
    def a_star_algorithm(self):
        start_node = Node(self.initial_state)
        open_list = [start_node]
        closed_set = set()

        while open_list:
            current_node = min(open_list, key=lambda x: x.depth + self.misplaced_tiles_heuristic(x.state))
            open_list.remove(current_node)

            if current_node.state == self.goal_state:
                return self.construct_path(current_node)

            # closed_set.add(tuple(map(tuple, current_node.state)))

            for child in current_node.generate_children():
                if tuple(map(tuple, child.state)) not in closed_set:
                    open_list.append(child)

            closed_set.add(tuple(map(tuple, current_node.state)))


        return None

    def construct_path(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
solver = PuzzleSolver(initial_state)
solution = solver.a_star_algorithm()
if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
