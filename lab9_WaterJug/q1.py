from typing import List, Tuple

class State:
    """Current state of the jugs."""
    def __init__(self, X=0, Y=0, rule=None):
        self.X = X
        self.Y = Y
        self.rule = rule
    
    def neighbors(self) -> List['State']:
        result = []
        max_x = max_jug.X
        max_y = max_jug.Y
        X, Y = self.X, self.Y

        if X < max_x: 
            result.append(State(max_x, Y, "Fill X")) # fill X
        if Y < max_y:
            result.append(State(X, max_y, "Fill Y")) # fill Y
        if X > 0:
            result.append(State(0, Y, "Empty X")) # empty X
        if Y > 0:
            result.append(State(X, 0, "Empty Y")) # empty Y
        if X + Y >= max_x and Y > 0:
            result.append(State(max_x, Y - (max_x - X), "Pour from Y to X")) # pour from Y to X
        if X + Y >= max_y and X > 0:
            result.append(State(X - (max_y - Y), max_y, "Pour from X to Y")) # pour from X to Y
        if X + Y <= max_x and Y > 0:
            result.append(State(X + Y, 0, "Pour all from Y to X")) # pour all from Y to X
        if X + Y <= max_y and X > 0:
            result.append(State(0, X + Y, "Pour all from X to Y")) # pour all from X to Y
        
        return result
    
    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y
    
    def __str__(self):
        return f"({self.X}, {self.Y}) [{self.rule}]"
    
    def __hash__(self):
        return hash((self.X, self.Y, self.rule))

def construct_path(prev, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()
    return path

def bfs(start, goal):
    frontier = [start]
    prev = {start: None}

    while frontier:
        current = frontier.pop(0)

        if current == goal:
            break

        for next in current.neighbors():
            if next not in prev:
                frontier.append(next)
                prev[next] = current

    return construct_path(prev, start, goal)

def dfs(start, goal):
    frontier = [start]
    prev = {start: None}

    while frontier:
        current = frontier.pop()

        if current == goal:
            break

        for next in current.neighbors():
            if next not in prev:
                frontier.append(next)
                prev[next] = current

    return construct_path(prev, start, goal)

def display_path(path):
    for state in path:
        print(state)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

print("Enter maximum capacities of the jugs:")
max_x = get_valid_input("Max capacity of X: ")
max_y = get_valid_input("Max capacity of Y: ")

print("\nEnter goal state:")
goal_x = get_valid_input("Goal for X jug: ")
goal_y = get_valid_input("Goal for Y jug: ")

max_jug = State(max_x, max_y)

start_state = State()
goal_state = State(goal_x, goal_y)

bfs_path = bfs(start_state, goal_state)
dfs_path = dfs(start_state, goal_state)

print("\nBFS Path:")
display_path(bfs_path)

print("\nDFS Path:")
display_path(dfs_path)
