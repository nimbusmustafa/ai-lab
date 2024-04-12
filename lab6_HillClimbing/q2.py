import random

def gen_states(queens, n):
    adList = []
    for i in range(n):
        if queens[i] < n - 1:
            node = queens[:i] + [queens[i] + 1] + queens[i + 1:]
            adList.append(node)
    return adList

def value(state, n):
    ans = 0
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[state[i]][i] = 1
    for i in range(n):
        for j in board[state[i]][i + 1:]:
            if j == 1:
                ans += 1
        for x, y in zip(range(state[i] + 1, n), range(i + 1, n)):
            if board[x][y] == 1:
                ans += 1
        for x, y in zip(range(state[i] - 1, -1, -1), range(i + 1, n)):
            if board[x][y] == 1:
                ans += 1
    return ans

def hill_climbing(n):
    # state = [random.randint(0, n-1) for _ in range(n)]  # Random initial state
    state=[0,1,2,3,4,5,6,7]
    print(f'Initial state: {state}')
    iterations = 0
    while True:
        adList = gen_states(state, n)
        flag = True
        for i in adList:
            if value(i, n) <= value(state, n):
                flag = False
                state = i
                break
        if flag:
            print(f'Solution found: {state}, value = {value(state, n)}')
            return

if __name__ == '__main__':
    hill_climbing(8)
