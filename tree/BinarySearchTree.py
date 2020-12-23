import json


class Node:
    def __init__(self, value):
        self.data = value
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


class BinarySearchTree:

    def __init__(self):
        self.root = None

    """新增二元樹節點"""

    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return self

        currentNode = self.root

        while currentNode is not None:
            # left
            if value < currentNode.data:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return self

                currentNode = currentNode.left

            # right
            elif value > currentNode.data:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return self

                currentNode = currentNode.right

            else:
                return self

    def lookup(self, value):
        if self.root is None:
            return None

        currentNode = self.root

        while currentNode is not None:
            # left
            if value < currentNode.data:
                currentNode = currentNode.left

            # right
            elif value > currentNode.data:
                currentNode = currentNode.right

            else:
                return currentNode

        return None

    """
    利用 recursive 找尋所有 node, 並用 json 表示
    recursive 過程可看 stack 圖示
    """

    def traverse(self, node):

        if node is None:
            return {}

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

    """
    在某一個 node 的左子樹中執行遞迴,
    到達最大值的 node 以後,重新指定其 parent node 的 right node.
    因為左子束中
    """

    def leftSubTree(self, node):
        pass

    def remove(self, value):
        currentNode = self.root
        parentNode = None

        while currentNode is not None:
            # 找到被刪除的 node
            if value == currentNode.data:
                # 被刪除的 node 沒有任何子節點
                if currentNode.left is None and currentNode.right is None:
                    if parentNode.left == currentNode:
                        parentNode.left = None
                    else:
                        parentNode.right = None

                # 被刪除的 node 沒有左節點
                elif currentNode.left is None:
                    if parentNode.left == currentNode:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right

                # 被刪除的 node 沒有右節點
                elif currentNode.right is None:
                    if parentNode.left == currentNode:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.right = currentNode.left

                # 被刪除的 node 有左右節點
                else:
                    pass

                return self

            # left
            elif value < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left

            # right
            elif value > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right


tree = BinarySearchTree()
tree.insert(15)
tree.insert(9)
tree.insert(23)
tree.insert(3)
tree.insert(12)
tree.insert(17)
tree.insert(1)
tree.insert(8)
tree.insert(4)

print(f"treeNode: {json.dumps(tree.traverse(tree.root))}")

# tree.remove(8)

# print(f"after remove treeNode: {json.dumps(tree.traverse(tree.root))}")

tmpNode = tree.lookup(9)
