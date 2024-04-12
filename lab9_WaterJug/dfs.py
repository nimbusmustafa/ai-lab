def genlist(x, y, max_x, max_y):
    adList = []
    if x < max_x:
        adList.append((max_x, y))
    if y < max_y:
        adList.append((x, max_y))
    if x > 0:
        adList.append((0, y))
    if y > 0:
        adList.append((x, 0))
    if x + y >= max_x and y > 0:
        adList.append((max_x, x + y - max_x))
    if x + y >= max_y and x > 0:
        adList.append((x + y - max_y, max_y))
    if x + y <= max_x and y > 0:
        adList.append((x + y, 0))
    if x + y <= max_y and x > 0:
        adList.append((0, x + y))
    return adList


def dfs(x, y, path, max_x, max_y, goal_x, goal_y):

    if x == goal_x and y == goal_y:
        print("Path to reach target configuration:")
        for step in path:
            print(step)
        exit()
    adList = genlist(x, y, max_x, max_y)
    for x in adList:
        n_path = list(path)  # Create a copy of the path list
        n_path.append((x[0], x[1]))
        dfs(x[0], x[1], n_path, max_x, max_y, goal_x, goal_y)

if __name__ == '__main__':
    max_x = int(input("Enter the maximum capacity of jug X: "))
    max_y = int(input("Enter the maximum capacity of jug Y: "))
    goal_x = int(input("Enter the final amount of water in jug X: "))
    goal_y = int(input("Enter the final amount of water in jug Y: "))
    dfs(0, 0, [], max_x, max_y, goal_x, goal_y)
