import json


class Node:
    def __init__(self, value):
        self.data = value
        self.height = None
        self.left = None
        self.right = None

    def __str__(self):
        leftData = None
        rightData = None
        if self.left is not None:
            leftData = self.left.data

        if self.right is not None:
            rightData = self.right.data

        return f"data:{self.data}, leftData:{leftData}, rightData:{rightData}"


"""
    平衡二元樹，新增時會觀察每個 Node 的平衡因子，在執行對應的 Rotation 
    調整每個 Node 的位置以增加後續搜尋的效率
"""


class AVLTree:

    def __init__(self):
        self.root = None

    def traverse(self, node):

        if node is None:
            return {}

        # 資料結構為 dictionary
        treeNode = {}

        treeNode["value"] = node.data

        # 先用 recursive 取得所有左邊的 node
        if node.left is not None:
            treeNode["left"] = self.traverse(node.left)
        else:
            treeNode["left"] = 'None'

        # 用 recursive 取得所有右邊的 node
        if node.right is not None:
            treeNode["right"] = self.traverse(node.right)
        else:
            treeNode["right"] = 'None'

        return treeNode

    """計算每個 Node 的高度"""

    def nodeHeight(self, node):
        hL = 0
        hR = 0

        if node is not None:
            if node.left is not None:
                hL = node.left.height
            elif node.right is not None:
                hR = node.right.height

        # 加 1 代表本身的高度
        if hL > hR:
            return hL + 1
        else:
            return hR + 1

    """計算每個 Node 的平衡因子"""

    def balanceFactor(self, node):

        hL = 0
        hR = 0

        if node is not None:
            if node.left is not None:
                hL = node.left.height
            elif node.right is not None:
                hR = node.right.height

        return hL - hR

    def llRotation(self, p):
        pl = p.left
        plr = pl.right

        # 中間值往上拉,小的放左邊,大的放右邊
        pl.right = p
        # 中間值的右子樹放在大值的左子樹
        p.left = plr

        # 有異動子樹的 Node 需重新計算高度
        pl.height = self.nodeHeight(pl)
        p.height = self.nodeHeight(p)

        if self.root == p:
            self.root = pl

        return pl

    def insert(self, node, value):

        newNode = None

        """新增節點"""
        if node is None:
            newNode = Node(value)
            newNode.height = 1
            return newNode

        if value < node.data:
            node.left = self.insert(node.left, value)
        elif value > node.data:
            node.right = self.insert(node.right, value)

        # Update height
        node.height = self.nodeHeight(node)

        # 執行 Balance Factor 檢核時，會檢核以下類型
        if self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == 1:
            return self.llRotation(node)

        return node


def main():
    avl_tree = AVLTree()

    avl_tree.root = avl_tree.insert(avl_tree.root, 30)
    avl_tree.root = avl_tree.insert(avl_tree.root, 20)
    avl_tree.root = avl_tree.insert(avl_tree.root, 40)
    avl_tree.root = avl_tree.insert(avl_tree.root, 10)
    avl_tree.root = avl_tree.insert(avl_tree.root, 25)
    avl_tree.root = avl_tree.insert(avl_tree.root, 50)
    avl_tree.root = avl_tree.insert(avl_tree.root, 5)
    avl_tree.root = avl_tree.insert(avl_tree.root, 13)
    avl_tree.root = avl_tree.insert(avl_tree.root, 28)

    avl_tree.traverse(avl_tree.root)

    print(f"avl_tree:{json.dumps(avl_tree.traverse(avl_tree.root))}")


main()
