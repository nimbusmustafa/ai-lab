class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def bfs(self, start, end):
        queue = [(start, [])]  # Queue stores (position, path)
        self.visited.append(start)

        while queue:
            current_pos, current_path = queue.pop(0)
            if current_pos == end:
                return current_path + [current_pos]

            for dr, dc in self.directions:
                new_row, new_col = current_pos[0] + dr, current_pos[1] + dc
                if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in self.visited:
                    queue.append(((new_row, new_col), current_path + [current_pos]))
                    self.visited.append((new_row, new_col))

        return None  
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

solver = MazeSolver(maze)
start = (0, 0)
end = (4, 4)
path = solver.bfs(start, end)

if path:
    print("Path found:", path)
else:
    print("No path found.")
