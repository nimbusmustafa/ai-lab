class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def heuristic(self, current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])  # Manhattan distance

    def a_star(self, start, end):
        queue = [(0, start, [])]  # (f-value, position, path)
        visited = set()

        while queue:
            queue.sort()  # Sort by f-value (ascending)
            _, current, path = queue.pop(0)

            if current == end:
                return path + [current]

            if current in visited:
                continue
            visited.add(current)

            for dr, dc in self.directions:
                new_row, new_col = current[0] + dr, current[1] + dc
                if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                    new_path = path + [current]
                    f = len(new_path) + self.heuristic((new_row, new_col), end)
                    queue.append((f, (new_row, new_col), new_path))

        return None  # If no path is found

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

solver = AStar(maze)
path = solver.a_star(start, end)

if path:
    print("Path found:", path)
else:
    print("No path found.")
