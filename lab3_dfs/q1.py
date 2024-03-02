class Graph:
    def topological(self, adList, visit, stack, curr):
        if curr in visit:
            return stack
        visit.append(curr)
        for x in adList[curr]:
            stack = self.topological(adList, visit, stack, x)
        stack.append(curr)
        return stack

if __name__ == '__main__':
    adList = {
        'A': ['D','C','B'],
        'B': ['E','F'],
        'C': ['A','F'],
        'D': ['A'],
        'E': ['B'],

        'F': ['B', 'C'],
    }

    vertices = []
    for node, neighbors in adList.items():
        if node not in vertices:
            vertices.append(node)
        for neighbor in neighbors:
            if neighbor not in vertices:
                vertices.append(neighbor)

    visit = []
    stack = []
    ob = Graph()

    for vertex in vertices:
        if vertex not in visit:
            stack = ob.topological(adList, visit, stack, vertex)

    stack = stack[::-1]
    print(stack)
