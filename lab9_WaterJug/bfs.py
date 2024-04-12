def genlist(x, y, max_x, max_y):
    adList = []
    if x < max_x:
        adList.append((max_x, y))
        # print("1")
    if y < max_y:
        adList.append((x, max_y))
        # print("2")

    if x > 0:
        adList.append((0, y))
        # print("3")

    if y > 0:
        # print("4")

        adList.append((x, 0))
    if x + y >= max_x and y > 0:
        adList.append((max_x, x + y - max_x))
        # print("5")

    if x + y >= max_y and x > 0:
        adList.append((x + y - max_y, max_y))
        # print("6")

    if x + y <= max_x and y > 0:
        adList.append((x + y, 0))
        # print("7")
# 
    if x + y <= max_y and x > 0:
        adList.append((0, x + y))
        # print("8")

  
    return adList

def bfs(max_x, max_y, target):
    queue, source = [[(0, 0), [(0, 0)]]], (0, 0)
    while queue:
        curr = queue.pop(0)
        if curr[0] == target:
            print("Path to reach target configuration:")
            for step in curr[1]:
                print(step)
            return
        adList = genlist(curr[0][0], curr[0][1], max_x, max_y)
        for x in adList:
            path = [step for step in curr[1]]
            path.append(x)
            node = [x, path]
            print(node)
            queue.append(node)
    print("Target configuration cannot be reached.")

if __name__ == '__main__':
    max_x = int(input("Enter capacity of jug X: "))
    max_y = int(input("Enter capacity of jug Y: "))
    target_x = int(input("Enter target amount of water in jug X: "))
    target_y = int(input("Enter target amount of water in jug Y: "))
    target = (target_x, target_y)
    bfs(max_x, max_y, target)
