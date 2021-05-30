import sys
from enum import Enum
from typing import Counter, TypeVar, Generic

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

    def search(self, key):
        current = self.root
        while current != self.leafnode and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return current

    """ current is left child fix case """

    def __fix_delete_case1(self, current):
        sibling = current.parent.right
        # case1. sibling is red
        if sibling.color == Color.RED:
            sibling.color = Color.BLACK
            current.parent.color = Color.RED
            self.left_rotate(current.parent)
            sibling = current.parent.right

        # 進入 Case2、3、4: sibling 是黑色

        # Case2: sibling的兩個child都是黑色
        if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
            sibling.color = Color.RED
            current = current.parent
        # Case3 & 4: current只有其中一個child是黑色
        else:
            # case3: sibling的right child是黑的, left child是紅色
            if sibling.right.color == Color.BLACK:
                sibling.left.color = Color.BLACK
                sibling.color = Color.RED
                self.right_rotate(sibling)
                sibling = current.parent.right

            # 經過Case3後, 一定會變成Case4
            # Case 4: sibling的right child 是紅色的, left child是黑色
            sibling.color = current.parent.color
            current.parent.color = Color.BLACK
            sibling.right.color = Color.BLACK
            self.left_rotate(current.parent)
            current = self.root  # 將current移動到 root, 一定跳出迴圈

        return current

    """ current is right child fix case """

    def __fix_delete_case2(self, current):
        sibling = current.parent.left
        # case1. sibling is red
        if sibling.color == Color.RED:
            sibling.color = Color.BLACK
            current.parent.color = Color.RED
            self.right_rotate(current.parent)
            sibling = current.parent.left

        # 進入 Case2、3、4: sibling 是黑色

        # Case2: sibling的兩個child都是黑色
        if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
            sibling.color = Color.RED
            current = current.parent
        # Case3 & 4: current只有其中一個child是黑色
        else:
            # case3: sibling 的 left child是黑的, right child是紅色
            if sibling.left.color == Color.BLACK:
                sibling.right.color = Color.BLACK
                sibling.color = Color.RED
                self.left_rotate(sibling)
                sibling = current.parent.left

            # 經過Case3後, 一定會變成Case4
            # Case 4: sibling 的 left child 是紅色的, right child是黑色
            sibling.color = current.parent.color
            current.parent.color = Color.BLACK
            sibling.left.color = Color.BLACK
            self.right_rotate(current.parent)
            current = self.root  # 將current移動到 root, 一定跳出迴圈

        return current

    def __fix_delete(self, current):
        # current.color 是 red, 直接塗黑
        # current 是 root, 直接塗黑

        while current != self.root and current.color == Color.BLACK:
            # current is left child
            if current == current.parent.left:
                current = self.__fix_delete_case1(current)
            # current is right child
            else:
                current = self.__fix_delete_case2(current)

        current.color = Color.BLACK

    """ 尋找右子樹最小值"""

    def getRightSubTreeMinNode(self, curretNode):
        if curretNode.right != self.leafnode:
            curretNode = curretNode.right
            while curretNode.left != self.leafnode:
                curretNode = curretNode.left

        return curretNode

    def delete(self, key):
        delete_node = self.search(key)

        if delete_node == self.leafnode:
            print(f"the key:{key} not found!!")
            return

        node_y = self.leafnode  # 真正被刪除的 node

        node_x = self.leafnode  # 真正被刪除 node 的 child

        if delete_node.left == self.leafnode or delete_node.right == self.leafnode:
            node_y = delete_node
        else:
            node_y = self.getRightSubTreeMinNode(
                delete_node
            )  # node_y 為 delete_node 右子樹的最大值

        if node_y.left != self.leafnode:
            node_x = node_y.left
        else:
            node_x = node_y.right

        # 將 node_x 取代 node_y
        node_x.parent = node_y.parent
        if node_y.parent == self.leafnode:  # 如果 node_y 原本為 root, 則 node_x 指定為 root
            self.root = node_x
        elif node_y == node_y.parent.left:
            node_y.parent.left = node_x
        else:
            node_y.parent.right = node_x

        # node_y 的值去取代 delete_node 的值
        if node_y != delete_node:
            delete_node.key = node_y.key
            delete_node.element = node_y.element

        # 若刪除的node是黑色, 要從x進行修正, 以符合RBT的顏色規則
        if node_y.color == Color.BLACK:
            self.__fix_delete(node_x)

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

        newNode = self.search(key)

        if newNode.key == key:
            print(f"the key: {key} has already inserted!!")
            return

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

    bst = RedBlackTree()

    bst.insert(70, "J")
    bst.insert(40, "T")
    bst.insert(100, "P")
    bst.insert(20, "I")
    bst.insert(50, "A")
    bst.insert(80, "Q")
    bst.insert(110, "L")
    bst.insert(10, "C")
    bst.insert(30, "D")
    bst.insert(90, "A")
    bst.insert(120, "G")

    bst.pretty_print()

    bst.delete(100)
    print(f"after delete:")
    bst.pretty_print()

    bst.delete(70)
    print(f"after delete:")
    bst.pretty_print()