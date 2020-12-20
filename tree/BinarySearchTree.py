import json


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


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

        def traverse(node):
            treeNode = {value: node.data}

            if node.left is not None:
                traverse(node.left)
            else:
                treeNode.left = None

            if node.right is not None:
                traverse(node.right)
            else:
                treeNode.right = None

            return treeNode
