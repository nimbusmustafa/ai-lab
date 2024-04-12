class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = []
        queue.append([])
        while queue:
            solution = queue.pop(0)
            print(solution)
            if self.conflict(solution):
                # print("loda")
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                # print(" ")
                # print(queen)
                queens = solution.copy()
                queens.append(queen)
                queue.append(queens)
        return solutions

    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in queens:
                    print(f'{j}, ', end='')
        print()    

def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    print_solutions = input('Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    bfs_solutions = n_queens.solve_bfs()
    if print_solutions:
        for i, solution in enumerate(bfs_solutions):
            print('BFS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total BFS solutions: %d' % len(bfs_solutions))

if __name__ == '__main__':
    main()
