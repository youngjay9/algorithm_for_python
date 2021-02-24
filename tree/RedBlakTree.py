import sys
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

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == Color.RED else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    """計算每個 Node 的高度"""

    def nodeHeight(self, node):
        hL = 0
        hR = 0

        if node is not None:
            if node.left is not None:
                hL = node.left.height

            if node.right is not None:
                hR = node.right.height

        # 加 1 代表本身的高度
        if hL > hR:
            return hL + 1
        else:
            return hR + 1

    def __fix_insert(self, k):
        while k.parent.color == Color.RED:
            pass

    def insert(self, node, key):
        """新增的節點"""

        if node is None:
            newNode = Node(key)
            newNode.left = None
            newNode.right = None
            newNode.color = Color.RED  # new node must be red
            newNode.height = 1
            return newNode

        if key < node.data:
            node.left = self.insert(node.left, key)
            # 指定 parent node
            node.left.parent = node
        elif key > node.data:
            node.right = self.insert(node.right, key)
            # 指定 parent node
            node.right.parent = node

        # Update height
        node.height = self.nodeHeight(node)

        return node


if __name__ == '__main__':

    rb_tree = RedBlackTree()
    rb_tree.root = rb_tree.insert(rb_tree.root, 10)
    rb_tree.root = rb_tree.insert(rb_tree.root, 20)

    print(f'root: {rb_tree.root.data}')

    rb_tree.pretty_print()
