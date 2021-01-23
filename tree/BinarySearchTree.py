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
    recursive 過程可看圖檔 traverse.jpg
    """

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

    """找出該 node 下的最大值"""

    def findMaxNode(self, node):
        if node is None:
            return None

        while node.right:
            node = node.right

        return node

    """
    在某一個 node 的左子樹中執行遞迴,
    到達最大值的 node 以後,重新指定其 parent node 的 right node.
    運作過程參考圖示：leftSubTree_1.jpg、leftSubTree_2.jpg
    """

    def leftSubTree(self, node):
        if node.right is None:
            newNode = node.left
            return newNode

        node.right = self.leftSubTree(node.right)

        return node

    def remove(self, value):
        currentNode = self.root

        parentNode = None

        while currentNode is not None:

            # 找到被刪除的 node
            if value == currentNode.data:

                newNode = None

                """刪除節點有以下3種情況"""
                # 被刪除的 node 沒有任何子節點
                if currentNode.left is None and currentNode.right is None:
                    pass

                # 被刪除的 node 沒有左節點
                elif currentNode.left is None:
                    # 指定新節點為刪除節點的右子節點
                    newNode = currentNode.right

                # 被刪除的 node 沒有右節點
                elif currentNode.right is None:
                    # 指定新節點為刪除節點的左子節點
                    newNode = currentNode.left

                # 被刪除的 node 有左右節點
                else:
                    # 從被刪除的節點,找它的左子樹中最大值的 node
                    leftTreeMaxNode = self.findMaxNode(currentNode.left)
                    # 左子樹最大值的節點去替換被刪除的節點
                    newNode = Node(leftTreeMaxNode.data)
                    # 因左子樹中的最大值已被拿去替換刪除節點,需再重新設定
                    newNode.left = self.leftSubTree(currentNode.left)

                """透過上層節點設定新節點"""
                if parentNode.left == currentNode:
                    parentNode.left = newNode
                else:
                    parentNode.right = newNode

                return self

            # 往左邊繼續找
            elif value < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left

            # 往右邊繼續找
            elif value > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right

        return self


tree = BinarySearchTree()
tree.insert(40)
tree.insert(29)
tree.insert(60)
tree.insert(25)
tree.insert(37)
tree.insert(20)
tree.insert(27)
tree.insert(35)
tree.insert(38)
tree.insert(26)
tree.insert(28)

print(f"treeNode: {json.dumps(tree.traverse(tree.root))}")


tree.remove(29)

print(f"after remove treeNode: {json.dumps(tree.traverse(tree.root))}")
