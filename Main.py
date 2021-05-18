from FunAndClass import*


def QueryY(tree, rect, total):
    coord = Coordinates(rect)

    v_spl = findSplitNode(tree, rect)

    if not v_spl:
        return 0
    if isLeaf(v_spl):
        if coord.yDn <= v_spl.key[1] <= coord.yUp:
            total += 1
    else:
        if coord.yDn <= v_spl.key[1] <= coord.yUp:
            total += 1
        v = v_spl.left
        while v:
            if coord.yDn <= v.key[1] <= coord.yUp:
                total += 1
            if coord.yDn <= v.key[1]:
                if v.right:
                    total += v.right.numNodes
                v = v.left
            else:
                v = v.right
        v = v_spl.right
        while v:
            if coord.yDn <= v.key[1] <= coord.yUp:
                total += 1
            if coord.yUp >= v.key[1]:
                if v.left:
                    total += v.left.numNodes
                v = v.right
            else:
                v = v.left
    return total


class Solution(object):
    def __init__(self, points):
        self.points = points
        self.tree = self.buildTree(points)

    def arrToTree(self, array):
        array = sorted(array, key=lambda x: x[1])
        length = len(array)

        if length == 0:
            return None

        if length == 1:
            new_node = BSTNode(array[0])
            new_node.numNodes = len(array)
            return new_node

        root = BSTNode(array[length // 2])
        root.left = self.arrToTree(array[:length // 2])
        root.right = self.arrToTree(array[length // 2 + 1:])
        root.numNodes = len(array)
        return root

    def buildTree(self, points):
        ytree = self.arrToTree(points)

        if len(points) == 0:
            return None

        if len(points) == 1:
            v = BSTNode(points[0])
            v.YTree = ytree
            v.range = [points[0][0], points[len(points) - 1][0]]
            return v
        else:
            points.sort()
            mid = (len(points) - 1) // 2
            xMed = points[mid]
            pL = points[: mid]
            pR = points[mid + 1:]
            v = BSTNode(xMed)
            v.left = self.buildTree(pL)
            v.right = self.buildTree(pR)
            v.YTree = ytree
            v.range = [points[0][0], points[len(points) - 1][0]]
            return v

    def Query(self, tree, rect):
        coord = Coordinates(rect)
        if (not tree) or tree.range[0] > coord.xUp or tree.range[1] < coord.xDn:
            return 0
        if isLeaf(tree):
            if coord.xDn <= tree.key[0] <= coord.xUp:
                if coord.yDn <= tree.key[1] <= coord.yUp:
                    return 1
            return 0
        if tree.range[0] >= coord.xDn and coord.xUp >= tree.range[1]:
            total = QueryY(tree.YTree, rect, 0)
            return total
        count = 0
        if coord.xDn <= tree.key[0] <= coord.xUp:
            if coord.yDn <= tree.key[1] <= coord.yUp:
                count += 1
        if tree.left:
            count += self.Query(tree.left, rect)
        if tree.right:
            count += self.Query(tree.right, rect)
        return count

    def query(self, rect) -> int:
        set_points = self.Query(self.tree, rect)
        return set_points


if __name__ == "__main__":
    points = [[1, 1], [3, 3], [2, 2], [1, 3]]
    sol = Solution(points)
    print(sol.query([[1, 3], [1, 3]]))  # 4
    print(sol.query([[1, 5], [2, 5]]))  # 3

    points = [[-2, 1], [0, 1], [2, 1], [-2, -1], [0, -1], [2, -1]]
    sol = Solution(points)
    print(sol.query([[0, 0], [-2, 2]]))  # 2
    print(sol.query([[1, 2], [0, 0]]))  # 0

    points = [[0, 0], [0, 0], [0, 0]]
    sol = Solution(points)
    print(sol.query([[0, 0], [0, 0]]))  # 3
