class MazeSolverUCS:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def get_neighbors(self, cell):
        neighbors = []
        row, col = cell
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            if self.is_valid_move(r, c):
                neighbors.append((r, c))
        return neighbors

    def ucs(self, start, end):
        queue = [(0, start, [])]  # (cost, position, path)
        visited = set()

        while queue:
            queue.sort()  # Sort by cost (ascending)
            cost, current, path = queue.pop(0)

            if current == end:
                return (path + [current],cost)

            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.get_neighbors(current):
                new_cost = cost + 1  # Uniform cost of 1 for each step
                new_path = path + [current]
                queue.append((new_cost, neighbor, new_path))

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
end = (3,4)

solver = MazeSolverUCS(maze)
path, cost = solver.ucs(start, end)

if path:
    print("Path found:", path)
    print(cost)
else:
    print("No path found.")
