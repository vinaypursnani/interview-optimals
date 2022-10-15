def depthFirstGraphTraversal(G):
    # first we need to get all the nodes
    nodesList = list(G.keys())

    # then we need to initialize our dfs stack with the node value that we need to start at
    dfStack = [nodesList[0]]

    # initializing an empty list for storing final dfs order
    finalOrder = []

    # we need to do the algo operation until our stack isn't empty
    while len(dfStack) != 0:

        # getting the current top most value from the stack
        currentValue = dfStack.pop()

        # storing that current value in the final order
        finalOrder.append(currentValue)

        # print(f'currentValue {currentValue}')
        # getting the nodes to which current value has directional edges

        thyNeighbours = list(G[currentValue])

        # appending each reachable edge from current value to our dfs stack
        for node in thyNeighbours:
            dfStack.append(node)

        # print(f'thyNeighbours {thyNeighbours}')

    # repeating until the stack isn't empty or in other sense we have looked at reachable neighbour nodes.
    # returning the final order

    return finalOrder



if __name__ == '__main__':
    G = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}
    print(depthFirstGraphTraversal(G))

