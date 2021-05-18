class BSTNode:
    def __init__(self, key):
        self.YTree = None
        self.key = key
        self.right = None
        self.left = None
        self.range = None
        self.numNodes = None
        self.root = None


class Coordinates:
    def __init__(self, rect):
        self.yUp = rect[1][1]
        self.yDn = rect[1][0]
        self.xUp = rect[0][1]
        self.xDn = rect[0][0]


def isLeaf(v):
    return v.left is None and v.right is None


def findSplitNode(tree, rect):
    coord = Coordinates(rect)
    if not tree:
        return None
    while not (coord.yUp >= tree.key[1] >= coord.yDn):
        if tree.key[1] < coord.yDn:
            tree = tree.right
        elif tree.key[1] > coord.yUp:
            tree = tree.left
        if not tree:
            return None
    return tree
