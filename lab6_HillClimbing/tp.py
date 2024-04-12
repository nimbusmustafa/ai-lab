import random

def heuristic(state):
    n = len(state)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def gen_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing():
    n = 8
    current_state = [0,0,0,0,0,0,0,0]
    path = [current_state.copy()]
    cost = [heuristic(current_state)]

    max_iter = 1000
    for _ in range(max_iter):
        neighbors = gen_neighbors(current_state)
        neighbors = [neighbor for neighbor in neighbors if neighbor != current_state]
        if not neighbors:
            break

        best_neighbor = min(neighbors, key=heuristic)
        best_neighbors = [neighbor for neighbor in neighbors if heuristic(neighbor) == heuristic(best_neighbor)]
        current_state = random.choice(best_neighbors)

        path.append(current_state.copy())
        cost.append(heuristic(current_state))

        if heuristic(current_state) == 0:
            break

    return current_state, path, cost

solution, path, cost = hill_climbing()
print("Solution:", solution)
# print("Path:", path)
print("Cost:", cost[-1])