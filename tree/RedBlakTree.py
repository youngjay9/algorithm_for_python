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


class LeafNode():
    def __init__(self):
        self.data = None
        self.color = Color.BLACK
        self.left = None
        self.right = None


class RedBlackTree():

    def __init__(self):
        self.leafnode = LeafNode()  # 為節省記憶體空間,提供其它 node 預設的 leafNode 都指向同一個 leafNode
        self.root = self.leafnode

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

    """right rotate(參考圖式)"""

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

        # 中間值:pr 的左子樹放在小值:p 的右邊
        prl = pr.left
        p.right = prl
        if prl != self.leafnode:
            prl.parent = p

        # p 原本是 root node,需換成 pr
        if p.parent == None:
            self.root = pr

        # 中間值往上拉
        pr.parent = p.parent

        if p == p.parent.left:
            p.parent.left = pr
        else:
            p.parent.right = pr

        # 小值放左邊
        pr.left = p
        p.parent = pr

    def __fix_insert(self, k):
        while k.parent.color == Color.RED:

            # P is right child of G
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle node

                # uncle is red
                # case 3.1 re-color
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    # 繼續進入下一個 while 檢查 great parent node
                    k = k.parent.parent

                # uncle is Black
                else:
                    # case 3.2.1
                    if k == k.parent.right:
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        self.left_rotate(k.parent.parent)
                    # case 3.2.2
                    elif k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        self.left_rotate(k.parent.parent)

            # P is left child of G
            else:
                u = k.parent.parent.right  # uncle node

                # uncle is red
                # case 3.1 re-color
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    # 繼續進入下一個 while 檢查 great parent node
                    k = k.parent.parent

                # uncle is black
                else:
                    # case 3.2.1
                    if k == k.parent.right:
                        k.parent.color = Color.BLACK
                        k.parent.parent.color = Color.RED
                        self.left_rotate(k.parent.parent)

            # 如果 k 為 root node, 則離開迴圈
            if k == self.root:
                break

        # end while loop

        self.root.color = Color.BLACK

    def insert(self, key):

        # 設定新節點
        newNode = Node(key)
        newNode.color = Color.RED
        newNode.parent = None
        newNode.left = self.leafnode
        newNode.right = self.leafnode

        tmpNode = self.root

        # 尋找新節點的 parent
        parentNode = None
        while tmpNode != self.leafnode:
            parentNode = tmpNode
            if key < tmpNode.data:
                tmpNode = tmpNode.left
            else:
                tmpNode = tmpNode.right

        newNode.parent = parentNode

        # parentNode 為 None, 代表第一次執行 insert, 需指定 root
        if parentNode == None:
            self.root = newNode

        # mew node 為 root, 設定 color: Black 直接 return
        if newNode.parent == None:
            newNode.color = Color.BLACK
            return

        # 指定新增 node 為 parent node 的 left or right
        if key < parentNode.data:
            parentNode.left = newNode
        elif key > parentNode.data:
            parentNode.right = newNode

        # 至少要有 3 個 node 再進行 fix
        if newNode.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert(newNode)


if __name__ == '__main__':

    rb_tree = RedBlackTree()

    rb_tree.insert(10)
    rb_tree.insert(10)

    rb_tree.pretty_print()
