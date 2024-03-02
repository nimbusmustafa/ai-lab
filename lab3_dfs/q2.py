class Graph:
    def topological(self, adList, visit, stack, curr):
        if curr in visit:
            raise ValueError("Cycle detected")
            
        visit.append(curr)
        for x in adList[curr]:
            stack = self.topological(adList, visit, stack, x)
        stack.append(curr)
        return stack

if __name__ == '__main__':
    adList = {
        '0': ['1','2'],
        '1': ['2'],
        '2': ['0','3'],
        '3':['3']
       
    }
    start_node='2'
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
     
    # for vertex in vertices:
    #     if vertex not in visit:
    #         stack = ob.topological(adList, visit, stack, vertex)

    if start_node in vertices:
        stack = ob.topological(adList, visit, stack, start_node)

    stack = stack[::-1]
    print(stack)
