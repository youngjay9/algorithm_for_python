import sys
from enum import Enum
from typing import TypeVar, Generic

T = TypeVar("T")


class Color(Enum):
    RED = 1
    BLACK = 0


class Node(Generic[T]):
    def __init__(self, key, element: T):
        self.key = key
        self.element = element
        self.color = None
        self.parent = None
        self.left = None
        self.right = None


class LeafNode:
    def __init__(self):
        self.key = 0
        self.element = None
        self.color = Color.BLACK
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.leafnode = LeafNode()  # 為節省記憶體空間,提供其它 node 預設的 leafNode 都指向同一個
        self.root = self.leafnode
        self.root.parent = self.leafnode

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

            print(str(node.key) + "(" + s_color + ")")

            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    def right_rotate(self, p):
        # 中間值: pl
        pl = p.left

        # 中間值:pl 的右子樹
        plr = pl.right

        # 中間值:pl 往上拉
        pl.parent = p.parent
        if p == p.parent.right:
            p.parent.right = pl
        else:
            p.parent.left = pl

        # p 原本是 root node,需換成 pl
        if p.parent == None:
            self.root = pl

        # 大值:p 放右邊
        pl.right = p
        p.parent = pl

        # 中間值的右子樹:plr 放大值:p 的左邊
        p.left = plr
        if plr != self.leafnode:
            plr.parent = p

    """left_rotate(參考圖式)"""

    def left_rotate(self, p):

        # 中間值: pr
        pr = p.right

        # 中間值:pr 的左子樹
        prl = pr.left

        # 中間值的左子樹放在小值:p 的右邊
        p.right = prl
        if prl != self.leafnode:
            prl.parent = p

        # 中間值:pr 往上拉
        pr.parent = p.parent
        if p == p.parent.left:
            p.parent.left = pr
        else:
            p.parent.right = pr

        # p 原本是 root node,需換成 pr
        if p.parent == None:
            self.root = pr

        # 小值放左邊
        pr.left = p
        p.parent = pr

    def __fix_insert_case1(self, current):
        uncle = current.parent.parent.right
        # case1: 若uncle是紅色
        if uncle.color == Color.RED:
            current.parent.color = Color.BLACK
            uncle.color = Color.BLACK
            current.parent.parent.color = Color.RED  # grandparent改成紅色
            current = current.parent.parent

        # case2 & 3: uncle是黑色
        else:
            # case2
            if current == current.parent.right:
                current = current.parent
                self.left_rotate(current)

            # case3
            current.parent.color = Color.BLACK  # 把parent塗黑
            current.parent.parent.color = Color.BLACK
            self.right_rotate(current.parent.parent)

        return current

    def __fix_insert_case2(self, current):

        uncle = current.parent.parent.left
        # case1: 若uncle是紅色
        if uncle.color == Color.RED:
            current.parent.color = Color.BLACK
            uncle.color = Color.BLACK
            current.parent.parent.color = Color.RED  # grandparent改成紅色
            current = current.parent.parent

        # case2 & 3: uncle是黑色
        else:
            # case2
            if current == current.parent.left:
                current = current.parent
                self.right_rotate(current)

            # case3
            current.parent.color = Color.BLACK  # 把parent塗黑
            current.parent.parent.color = Color.BLACK
            self.left_rotate(current.parent.parent)

        return current

    def __fix_insert(self, current):
        while current.parent.color == Color.RED:
            # parent是 grandparent的 left child
            if current.parent == current.parent.parent.left:
                current = self.__fix_insert_case1(current)
            # parent是 grandparent的 right child(與上面對稱)
            else:
                current = self.__fix_insert_case2(current)

        # 確保root是黑色
        self.root.color = Color.BLACK

    def insert(self, key, element: T):

        # 設定新節點
        newNode = Node(key, element)
        newNode.color = Color.RED
        newNode.parent = self.leafnode
        newNode.left = self.leafnode
        newNode.right = self.leafnode

        tmpNode = self.root

        # 尋找新節點的 parent
        parentNode = None

        while tmpNode != self.leafnode:
            parentNode = tmpNode
            if key < tmpNode.key:
                tmpNode = tmpNode.left
            elif key > tmpNode.key:
                tmpNode = tmpNode.right

        # parentNode 為 None, 代表第一次執行 insert, 需指定 root
        if parentNode == None:
            # mew node 為 root, 設定 color: Black 直接 return
            self.root = newNode
            self.root.color = Color.BLACK
            return
        else:
            newNode.parent = parentNode

        # 指定 newNode 為 parent node 的 left or right
        if key < parentNode.key:
            parentNode.left = newNode
        elif key > parentNode.key:
            parentNode.right = newNode

        # Fix the tree
        self.__fix_insert(newNode)


if __name__ == "__main__":

    newNode = Node("1", "0981253679")

    print(f"element:{newNode.element}")

    bst = RedBlackTree()

    bst.insert(50, "J")
    bst.insert(20, "T")
    bst.insert(70, "P")
    bst.insert(10, "I")
    bst.insert(40, "A")
    bst.insert(60, "Q")
    bst.insert(80, "L")
    bst.insert(30, "C")
    bst.insert(75, "D")

    bst.pretty_print()