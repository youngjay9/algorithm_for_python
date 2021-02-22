from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.color = None
        self.parent = None
        self.left = None
        self.right = None
        self.height = None


class RedBlackTree():
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        newNode = None

        """新增的節點"""
        newNode = Node(key)
        newNode.parent = None
        newNode.data = key
        newNode.left = None
        newNode.right = None
        newNode.color = Color.RED  # new node must be red
        newNode.height = 1


if __name__ == '__main__':

    print(f'red:{Color.RED}')
