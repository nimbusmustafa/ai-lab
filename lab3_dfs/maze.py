def solve_maze(maze, start, end):
    def dfs(current):
        nonlocal path
        if current == end:
            return True
        visited.add(current)
        for next_cell in get_neighbors(current):
            if next_cell not in visited:
                path.append(next_cell)
                if dfs(next_cell):
                    return True
                path.pop()  
        return False

    def get_neighbors(cell):
        neighbors = []
        row, col = cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '#':
                neighbors.append((r, c))
        return neighbors

    path = [start]
    visited = set()
    if dfs(start):
        print("Path to exit the maze:")
        for cell in path:
            print(cell)
    else:
        print("No path found!")

maze = [
    ['0', '#', '0', '0', '0'],
    ['0', '0', '#', '#', '0'],
    ['#', '0', '#', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['#', '#', '#', '0', '0']
]

start = (0, 0) 
end = (4, 4)    

solve_maze(maze, start, end)
