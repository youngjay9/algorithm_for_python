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

            if node.right is not None:
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

        if node is not None and node.left is not None:
            hL = node.left.height

        if node is not None and node.right is not None:
            hR = node.right.height

        return hL - hR

    def LLRotation(self, p):
        pl = p.left
        plr = pl.right

        # 中間值往上拉,小的放左邊,大的放右邊
        pl.right = p
        # 中間值的右子樹放在大值的左子樹
        p.left = plr

        # 有異動子樹的 Node 需重新計算高度
        # 需注意：因為 p 是在 pl 的子樹需先計算 p 的高度，再計算 pl 的高度
        p.height = self.nodeHeight(p)
        pl.height = self.nodeHeight(pl)

        if self.root == p:
            self.root = pl

        return pl

    def LRRotation(self, p):
        pl = p.left
        # 中間值
        plr = pl.right

        # 中間值的左子樹放小的右邊
        pl.right = plr.left
        # 中間值的右子樹放大的左邊
        p.left = plr.right

        # 中間值往上拉,小的放左邊,大的放右邊
        plr.left = pl
        plr.right = p

        # 有異動子樹的 Node 都需重新計算高度
        # 需注意：在下層的 node 需先計算高度
        pl.height = self.nodeHeight(pl)
        p.height = self.nodeHeight(p)
        plr.height = self.nodeHeight(plr)

        if self.root == p:
            self.root = plr

        return plr

    def RRRotation(self, p):
        # 中間值
        pr = p.right
        prl = pr.left

        # 中間值的左子樹放在小的右邊
        p.right = prl

        # 中間值往上拉,小的放左邊,大的放右邊
        pr.left = p

        # 有異動子樹的 Node 都需重新計算高度
        # 需注意：在下層的 node 需先計算高度
        p.height = self.nodeHeight(p)
        pr.height = self.nodeHeight(pr)

        if self.root == p:
            self.root = pr

        return pr

    def RLRotation(self, p):
        # 大值
        pr = p.right

        # 中間值
        prl = pr.left

        # 中間值的左子樹放小的右邊
        p.right = prl.left

        # 中間值的右子樹放大的左邊
        pr.left = prl.right

        # 中間值往上拉,小的放左邊,大的放右邊
        prl.left = p
        prl.right = pr

        # 有異動子樹的 Node 都需重新計算高度
        # 需注意：在下層的 node 需先計算高度
        pr.height = self.nodeHeight(pr)
        p.height = self.nodeHeight(p)
        prl.height = self.nodeHeight(prl)

        if self.root == p:
            self.root = prl

        return prl

    """ 尋找左子樹中最大值的 Node"""

    def findLeftSubTreeMaxNode(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node

    """ 尋找右子樹中最小值的 Node"""

    def findRightSubTreeMinNode(self, node):
        while node is not None and node.left is not None:
            node = node.left
        return node

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

        bf = self.balanceFactor(node)

        bfL = self.balanceFactor(node.left)

        bfR = self.balanceFactor(node.right)

        print(
            f"insert: {value} node value:{node.data} bf:{bf}, bfL:{bfL}, bfR:{bfR}")

        # 用 3 個 Node 執行 Balance Factor 檢核
        if self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == 1:
            return self.LLRotation(node)

        elif self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == -1:
            return self.LRRotation(node)

        elif self.balanceFactor(node) == -2 and self.balanceFactor(node.right) == -1:
            return self.RRRotation(node)

        elif self.balanceFactor(node) == -2 and self.balanceFactor(node.right) == 1:
            return self.RLRotation(node)

        return node

    def remove(self, node, value):
        if node is None:
            return None

        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
            del node
            return None

        if value < node.data:
            node.left = self.remove(node.left, value)

        elif value > node.data:
            node.right = self.remove(node.right, value)

        # 找到刪除的 Node
        else:
            q = None
            # 左子樹高度 大於右子樹
            if self.nodeHeight(node.left) > self.nodeHeight(node.right):
                # 從左子樹中找最大值的 Node 取代被刪除的 Node
                q = self.findLeftSubTreeMaxNode(node.left)
                node.data = q.data
                # 左子樹中最大值的 Node 需被刪除
                node.left = self.remove(node.left, q.data)
            else:
                # 從右子樹中找最小值的 Node 取代被刪除的 Node
                q = self.findRightSubTreeMinNode(node.right)
                node.data = q.data
                node.right = self.remove(node.right, q.data)

        # Update height
        node.height = self.nodeHeight(node)

        # 用 3 個 Node 執行 Balance Factor 檢核
        if self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == 1:
            return self.LLRotation(node)

        elif self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == -1:
            return self.LRRotation(node)

        elif self.balanceFactor(node) == -2 and self.balanceFactor(node.right) == -1:
            return self.RRRotation(node)

        elif self.balanceFactor(node) == -2 and self.balanceFactor(node.right) == 1:
            return self.RLRotation(node)
        # remove 的情境需多做以下 2 種 BF 的判斷
        elif self.balanceFactor(node) == 2 and self.balanceFactor(node.left) == 0:
            return self.LLRotation(node)

        elif self.balanceFactor(node) == -2 and self.balanceFactor(node.right) == 0:
            return self.RRRotation(node)

        return node


def main():
    avl_tree = AVLTree()

    # testing LRRotation
    # avl_tree.root = avl_tree.insert(avl_tree.root, 50)
    # avl_tree.root = avl_tree.insert(avl_tree.root, 10)
    # avl_tree.root = avl_tree.insert(avl_tree.root, 20)
    # avl_tree.traverse(avl_tree.root)

    avl_tree.root = avl_tree.insert(avl_tree.root, 10)
    avl_tree.root = avl_tree.insert(avl_tree.root, 20)
    avl_tree.root = avl_tree.insert(avl_tree.root, 30)
    avl_tree.root = avl_tree.insert(avl_tree.root, 25)
    avl_tree.root = avl_tree.insert(avl_tree.root, 28)
    avl_tree.root = avl_tree.insert(avl_tree.root, 27)
    avl_tree.root = avl_tree.insert(avl_tree.root, 5)

    print(f"avl_tree:{json.dumps(avl_tree.traverse(avl_tree.root))}")

    avl_tree.remove(avl_tree.root, 25)

    print(
        f"after remove 28, avl_tree:{json.dumps(avl_tree.traverse(avl_tree.root))}")


main()
