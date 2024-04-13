class HillClimbingMazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid_move(self, row, col):
        # print((row,col))
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == 0

    def distance(self, cell1, cell2):
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

    def get_neighbors(self, cell):
        neighbors = []
        row, col = cell
        for dr, dc in self.directions:
            r, c = row + dr, col + dc
            if self.is_valid_move(r, c):
                neighbors.append((r, c))
        return neighbors

    def solve(self, start, end):
        current = start
        path = [current]

        while current != end:
            neighbors = self.get_neighbors(current)
            next_cell = min(neighbors, key=lambda cell: self.distance(cell, end))
            print(next_cell)
            if next_cell == current:
                break

            current = next_cell
            path.append(current)

        if current == end:
            print("Path to exit the maze:")
            for cell in path:
                print(cell)
        else:
            print("No path found!")

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
  
]
start = (0, 0)
end = (4,4)

solver = HillClimbingMazeSolver(maze)
solver.solve(start, end)
