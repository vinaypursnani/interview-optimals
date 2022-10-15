from breadthFirstGraphTraversal import breadthFirstGraphTraversal
from depthFirstGraphTraversal import depthFirstGraphTraversal

def hasPath(G, src, dst, traverseType = 'BF'):
    if traverseType == 'BF':
        print(f'Using Breadth First Traverse type to find possible path from {src} to {dst}')
        myBFTOrder = breadthFirstGraphTraversal(G)
        myBFTOrderLength = len(myBFTOrder)

        for i in range(myBFTOrderLength):
            if myBFTOrder[i] == src:
                for j in range(i, myBFTOrderLength):
                    if myBFTOrder[j] == dst:
                        return True
        else:
            return False
    elif traverseType == 'DF':
        print(f'Using Depth First Traverse type to find possible path from {src} to {dst}')
        myDFTOrder = depthFirstGraphTraversal(G)
        myDFTOrderLength = len(myDFTOrder)

        for i in range(len(myDFTOrder)):
            for j in range(i, myDFTOrderLength):
                if myDFTOrder[j] == dst:
                    return True
        else:
            return False
    else:
        print(" Traverse type can be either 'DF' or 'BF'.")



if __name__ == '__main__':
    G = {'f': ['g', 'i'], 'g': ['h'], 'h': [], 'i': ['g', 'k'], 'j': ['i'], 'k': []}
    print(hasPath(G, 'f', 'j', 'DF'))
