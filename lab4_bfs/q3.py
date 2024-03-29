def calculate_total_distance(route, adjacency_list):
    total_distance = 0
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        for neighbor, dist in adjacency_list[current_city]:
            if neighbor == next_city:
                total_distance += dist
                break

    # Handle the distance from the last city back to the first city
    last_city = route[-1]
    first_city = route[0]
    for neighbor, dist in adjacency_list[last_city]:
        if neighbor == first_city:
            total_distance += dist
            break

    return total_distance

def traveling_salesman_dfs(graph, start):
    num_cities = len(graph)
    visited = set()
    route = [start]
    min_distance = float('inf')
    optimal_route = None

    def dfs(node):
        nonlocal min_distance, optimal_route
        if len(route) == num_cities:
            distance = calculate_total_distance(route, graph)
            if distance < min_distance:
                min_distance = distance
                optimal_route = route.copy()
            return

        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                route.append(neighbor)
                dfs(neighbor)
                route.pop()

        visited.remove(node)

    dfs(start)

    return optimal_route, min_distance

if __name__ == "__main__":
    adjacency_list = {
        '0': [('1', 20), ('2', 10), ('3', 12)],
        '1': [('0', 20), ('2', 15), ('3', 11)],
        '2': [('0', 10), ('1', 15), ('3', 17)],
        '3': [('1', 11), ('2', 17), ('0', 12)]
    }

    start_city = '0'  

    optimal_route, min_distance = traveling_salesman_dfs(adjacency_list, start_city)

    print("Optimal Route:", optimal_route)
    print("Minimum Distance:", min_distance)
