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

    def nodeheight(self, node):
        hL = 0
        hR = 0

        if node is not None:
            if node.left is not None:
                hL = node.left.height
            elif node.right is not None:
                hR = node.right.height

        if hL > hR:
            return hL + 1
        else:
            return hR + 1

    def insert(self, node, value):

        newNode = None

        """新增節點"""
        if node is None:
            newNode = Node(value)
            newNode.height = 1
            return newNode

        if value < node.left:
            node.left = self.insert(node.left, value)
        elif value > node.right:
            node.right = self.insert(node.right, value)

        # Update height
        node.height = nodeHeight(node)

        # 執行 Balance Factor 檢核時，會檢核以下類型


def main():
    avl_tree = AVLTree()

    avl_tree.root = avl_tree.insert(avl_tree.root, 10)

    avl_tree.traverse(avl_tree.root)

    print(f"avl_tree:{json.dumps(avl_tree.traverse(avl_tree.root))}")


main()
