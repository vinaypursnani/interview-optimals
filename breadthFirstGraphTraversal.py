def breadthFirstGraphTraversal(G):
    # first we need to get all the nodes
    nodeList = list(G.keys())

    # then we initialize our Breadth first queue with the element we want to start at
    bfQueue = [nodeList[0]]

    # final Breadth First Traversal order
    finalOrder = []

    # we need to do the algo operation until our queue isn't empty
    while len(bfQueue) != 0:
        currentValue = bfQueue.pop()
        # print(f'currentValue {currentValue}')

        finalOrder.append(currentValue)

        thyNeighbours = G[currentValue]
        # print(f'thyNeighbours {thyNeighbours}')
        for node in thyNeighbours:
            # print(node)
            bfQueue.insert(0, node)
            # print(bfQueue)

    return finalOrder


if __name__ == '__main__':
    G = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}
    print(breadthFirstGraphTraversal(G))
