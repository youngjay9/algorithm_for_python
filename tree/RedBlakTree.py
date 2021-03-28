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
        self.parent = None
        self.height = 1


class RedBlackTree():

    def __init__(self):
        self.leafnode = LeafNode()  # 為節省記憶體空間,提供其它 node 預設的 leafNode 都指向同一個
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

            print(str(node.data) + "(" + s_color + ")" +
                  "(" + str(node.height) + ")")

            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    """新增 Node 時重新計算高度"""

    def nodeHeightPlus(self, node, leftPlus):
        hL = 0
        hR = 0

        if node.left != self.leafnode:
            hL = node.left.height

        if node.right != self.leafnode:
            hR = node.right.height

        if leftPlus:
            hL = hL + 1
        else:
            hR = hR + 1

        # 加 1 代表本身的高度
        if node == self.root:
            if hL > hR:
                return hL
            else:
                return hR
        else:
            if hL > hR:
                return hL + 1
            else:
                return hR + 1

    """計算每個 Node 的平衡因子"""

    def balanceFactor(self, node):

        hL = 0
        hR = 0

        if node != self.leafnode and node.left != self.leafnode:
            hL = node.left.height

        if node != self.leafnode and node.right != self.leafnode:
            hR = node.right.height

        return hL - hR

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

    """計算每個 Node 的高度"""

    def nodeHeight(self, node):
        hL = 0
        hR = 0

        if node != self.leafnode:
            if node.left != self.leafnode:
                hL = node.left.height

            if node.right != self.leafnode:
                hR = node.right.height

        # 加 1 代表本身的高度
        if hL > hR:
            return hL + 1
        else:
            return hR + 1

    """loop 上去更新 parent 的 height"""

    def loop_update_parent_node_height(self, n):
        tmpParent = n.parent
        while tmpParent != None:
            tmpParent.height = self.nodeHeight(tmpParent)
            tmpParent = tmpParent.parent

    def LLRotation(self, p):
        # 中間值
        pl = p.left

        # 中間值的右子樹
        plr = pl.right

        # 中間值的右子樹放在大值的左子樹
        p.left = plr
        if plr != self.leafnode:
            plr.parent = p

        # 中間值往上拉
        pl.parent = p.parent

        if p.parent != None:
            if p.parent.left == p:
                p.parent.left = pl
            else:
                p.parent.right = pl

        # 小的放左邊(小值原本就在 pl 的左邊,所以不進行任何操作)

        # 大的放右邊
        pl.right = p
        p.parent = pl

        # 有異動子樹的 Node 需重新計算高度
        # 需注意：因為 p 是在 pl 的子樹需先計算 p 的高度，再計算 pl 的高度
        p.height = self.nodeHeight(p)
        pl.height = self.nodeHeight(pl)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(pl)

        # 中間值需變為 black
        pl.color = Color.BLACK

        # 小值及大值變為 red
        if pl.left != self.leafnode:
            pl.left.color = Color.RED

        if pl.right != self.leafnode:
            pl.right.color = Color.RED

        # 原本的 p 是 root 的話需替換成 pl
        if self.root == p:
            self.root = pl

        return pl

    def DEL_LLRotation(self, p):
        # 中間值
        pl = p.left

        # 中間值的右子樹
        plr = pl.right

        # 中間值: pl 往上拉
        pl.parent = p.parent
        if p.parent != None:
            if p.parent.left == p:
                p.parent.left = pl
            else:
                p.parent.right = pl

        # 原本的 p 是 root 的話需替換成 pl
        if self.root == p:
            self.root = pl

        self.root.color = Color.BLACK

        # 小的放左邊(小值原本就在 pl 的左邊,所以不進行任何操作)

        # 大值: p 放中間值: pl 右邊
        pl.right = p
        p.parent = pl

        # 中間值的右子樹: plr 放在大值: p 的左子樹
        p.left = plr

        # 如果中間值的右子樹: plr 不為 leafnode 再進行下列動作
        reassign_p = False

        if plr != self.leafnode:
            plr.parent = p

            # 檢查大值: p 的 balance factor 與中間值右子樹第一個 node: plr 的 balance factor
            bf_p = self.balanceFactor(p)
            bf_plr = self.balanceFactor(plr)

            if bf_p >= 2 and bf_plr >= 0:
                p = self.DEL_LLRotation(p)
                reassign_p = True
            elif bf_p >= 2 and bf_plr <= -1:
                p = self.DEL_LRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_plr <= -1:
                p = self.DEL_RRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_plr >= 0:
                p = self.DEL_RLRotation(p)
                reassign_p = True

        # 重新指定大值: p 放中間值: pl 右邊
        if reassign_p == True:
            pl.right = p
            p.parent = pl

        """
            有異動子樹的 Node 需重新計算高度
            需注意：因為 p 是在 pl 的子樹需先計算 p 的高度，再計算 pl 的高度
        """
        p.height = self.nodeHeight(p)
        pl.height = self.nodeHeight(pl)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(pl)

        return pl

    def LRRotation(self, p):
        # 小值
        pl = p.left

        # 中間值
        plr = pl.right

        # 中間值的左子樹放小值: pl 的右邊
        pl.right = plr.left
        if plr.left != self.leafnode:
            plr.left.parent = pl

        # 中間值的右子樹放大值: p的左邊
        p.left = plr.right
        if plr.right != self.leafnode:
            plr.right.parent = p

        # 中間值往上拉
        plr.parent = p.parent

        if p.parent != None:
            if p.parent.left == p:
                p.parent.left = plr
            else:
                p.parent.right = plr

        # 小的放左邊
        plr.left = pl
        pl.parent = plr

        # 大的放右邊
        plr.right = p
        p.parent = plr

        # 有異動子樹的 Node 都需重新計算高度
        # 需注意：在下層的 node 需先計算高度
        pl.height = self.nodeHeight(pl)
        p.height = self.nodeHeight(p)
        plr.height = self.nodeHeight(plr)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(plr)

        # 中間值需變為 black
        plr.color = Color.BLACK

        # 小值及大值變為 red
        if plr.left != self.leafnode:
            pl.left.color = Color.RED

        if plr.right != self.leafnode:
            plr.right.color = Color.RED

        # 原本的 p 是 root 的話需替換成 plr
        if self.root == p:
            self.root = plr

        return plr

    def DEL_LRRotation(self, p):
        # 小值
        pl = p.left

        # 中間值
        plr = pl.right

        # 中間值的左子樹
        plrl = plr.left

        # 中間值的右子樹
        plrr = plr.right

        # 中間值: plr 往上拉
        plr.parent = p.parent
        if p.parent != None:
            if p.parent.left == p:
                p.parent.left = plr
            else:
                p.parent.right = plr

        # 原本的 p 是 root 的話需替換成 plr
        if self.root == p:
            self.root = plr

        self.root.color = Color.BLACK

        # 小值: pl 放中間值: plr 左邊
        plr.left = pl
        pl.parent = plr

        # 中間值的左子樹: plrl 放小值: pl 的右邊
        pl.right = plrl

        # 如果中間值的左子樹: plrl 不是 leafnode 再進行下列動作
        reassign_pl = False

        if plrl != self.leafnode:
            plrl.parent = pl

            # 檢查小值: pl 的 balance factor 與中間值左子樹第一個 node: plrl 的 balance factor
            bf_pl = self.balanceFactor(pl)
            bf_plrl = self.balanceFactor(plrl)

            if bf_pl >= 2 and bf_plrl >= 0:
                pl = self.DEL_LLRotation(pl)
                reassign_pl = True
            elif bf_pl >= 2 and bf_plrl <= -1:
                pl = self.DEL_LRRotation(pl)
                reassign_pl = True
            elif bf_pl <= -2 and bf_plrl <= -1:
                pl = self.DEL_RRRotation(pl)
                reassign_pl = True
            elif bf_pl <= -2 and bf_plrl >= 0:
                pl = self.DEL_RLRotation(pl)
                reassign_pl = True

        # 重新指定小值: pl 放中間值: plr 的左邊
        if reassign_pl == True:
            plr.left = pl
            pl.parent = plr

        # 大值: p 放中間值:plr 的右邊
        plr.right = p
        p.parent = plr

        # 中間值的右子樹:plrr 放大值: p 的左邊
        p.left = plrr

        # 如果中間值的右子樹:不為 leafnode  再進行下列動作
        reassign_p = False

        if plrr != self.leafnode:
            plrr.parent = p

            # 檢查大值: p 的 balance factor 與中間值右子樹第一個 node: plrr 的 balance factor
            bf_p = self.balanceFactor(p)
            bf_plrr = self.balanceFactor(plrr)

            if bf_p >= 2 and bf_plrr >= 0:
                p = self.DEL_LLRotation(p)
                reassign_p = True
            elif bf_p >= 2 and bf_plrr <= -1:
                p = self.DEL_LRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_plrr <= -1:
                p = self.DEL_RRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_plrr >= 0:
                p = self.DEL_RLRotation(p)
                reassign_p = True

        # 重新指定大值: p 放中間值:plr 的右邊
        if reassign_p == True:
            plr.right = p
            p.parent = plr

        """
            有異動子樹的 Node 都需重新計算高度
            需注意：在下層的 node 需先計算高度
        """
        pl.height = self.nodeHeight(pl)

        p.height = self.nodeHeight(p)

        plr.height = self.nodeHeight(plr)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(plr)

        return plr

    def RRRotation(self, p):

        # 中間值
        pr = p.right

        # 中間值:pr 的左子樹
        prl = pr.left

        # 中間值的左子樹: prl 放在小的右邊
        p.right = prl

        if prl != self.leafnode:
            prl.parent = p

        # 中間值往上拉
        pr.parent = p.parent

        if p.parent != None:
            if p == p.parent.left:
                p.parent.left = pr
            else:
                p.parent.right = pr

        # 小的放左邊
        pr.left = p
        p.parent = pr

        # 大的放右邊(原本就已在 pr 的右邊,所以不進行任何動作)

        """
        有異動子樹的 Node 都需重新計算高度
        需注意：在下層的 node 需先計算高度
        """
        p.height = self.nodeHeight(p)

        pr.height = self.nodeHeight(pr)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(pr)

        # 中間值需變為 black
        pr.color = Color.BLACK

        # 小值及大值變為 red
        if pr.left != self.leafnode:
            pr.left.color = Color.RED
        if pr.right != self.leafnode:
            pr.right.color = Color.RED

        # 原本的 p 是 root 的話需替換成 pr
        if self.root == p:
            self.root = pr

        return pr

    def DEL_RRRotation(self, p):
        # 中間值
        pr = p.right

        # 中間值:pr 的左子樹
        prl = pr.left

        # 中間值往上拉
        pr.parent = p.parent

        if p.parent != None:
            if p == p.parent.left:
                p.parent.left = pr
            else:
                p.parent.right = pr

        # 原本的 p 是 root 的話需替換成 pr
        if self.root == p:
            self.root = pr

        self.root.color = Color.BLACK

        # 小值:p 放中間值左邊
        pr.left = p
        p.parent = pr

        # 大的放右邊(原本就已在 pr 的右邊,所以不進行任何動作)

        # 中間值的左子樹: prl 放在小值的右邊
        p.right = prl

        # 中間值的左子樹: prl 不為 leafnode 再進行下列動作
        reassign_p = False

        if prl != self.leafnode:
            prl.parent = p

            # 檢查小值的 balance factor 與中間值左子樹第一個 node 的 balance factor
            bf_p = self.balanceFactor(p)
            bf_prl = self.balanceFactor(prl)

            if bf_p >= 2 and bf_prl >= 0:
                p = self.DEL_LLRotation(p)
                reassign_p = True
            elif bf_p >= 2 and bf_prl <= -1:
                p = self.DEL_LRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_prl <= -1:
                p = self.DEL_RRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_prl >= 0:
                p = self.DEL_RLRotation(p)
                reassign_p = True

        # 重新指定小值:p 放中間值左邊
        if reassign_p == True:
            pr.left = p
            p.parent = pr

        """
        有異動子樹的 Node 都需重新計算高度
        需注意：在下層的 node 需先計算高度
        """
        p.height = self.nodeHeight(p)
        pr.height = self.nodeHeight(pr)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(pr)

        return pr

    def RLRotation(self, p):
        # 大值
        pr = p.right
        # 中間值
        prl = pr.left

        # 中間值的左子樹放小的右邊
        p.right = prl.left
        if prl.left != self.leafnode:
            prl.left.parent = p

        # 中間值的右子樹放大的左邊
        pr.left = prl.right
        if prl.right != self.leafnode:
            prl.right.parent = pr

        # 中間值:pr 往上拉
        prl.parent = p.parent

        if p.parent != None:
            if p == p.parent.left:
                p.parent.left = prl
            else:
                p.parent.right = prl

        # 小值放左邊
        prl.left = p
        p.parent = prl

        # 大值放右邊
        prl.right = pr
        pr.parent = prl

        # 有異動子樹的 Node 都需重新計算高度
        # 需注意：在下層的 node 需先計算高度
        pr.height = self.nodeHeight(pr)
        p.height = self.nodeHeight(p)
        prl.height = self.nodeHeight(prl)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(prl)

        # 中間值需變為 black
        prl.color = Color.BLACK

        # 小值及大值變為 red
        if prl.left != self.leafnode:
            prl.left.color = Color.RED

        if prl.right != self.leafnode:
            prl.right.color = Color.RED

        # 原本的 p 是 root 的話需替換成 prl
        if self.root == p:
            self.root = prl

        return prl

    def DEL_RLRotation(self, p):
        # 大值
        pr = p.right
        # 中間值
        prl = pr.left
        # 中間值的左子樹
        prll = prl.left
        # 中間值的右子樹
        prlr = prl.right

        # 中間值:prl 往上拉
        prl.parent = p.parent
        if p.parent != None:
            if p == p.parent.left:
                p.parent.left = prl
            else:
                p.parent.right = prl

        # 原本的 p 是 root 的話需替換成 prl
        if self.root == p:
            self.root = prl

        self.root.color = Color.BLACK

        # 小值: p 放中間值:prl 的左邊
        prl.left = p
        p.parent = prl

        # 中間值的左子樹: prll 放小值: p 的右邊
        p.right = prll

        # 如果中間值的左子樹: prll 不為 leafnode 再進行下列動作
        reassign_p = False

        if prll != self.leafnode:
            prll.parent = p

            # 檢查小值:p 的 balance factor 與中間值左子樹第一個 node:prll  的 balance factor
            bf_p = self.balanceFactor(p)
            bf_prll = self.balanceFactor(prll)

            if bf_p >= 2 and bf_prll >= 0:
                p = self.DEL_LLRotation(p)
                reassign_p = True
            elif bf_p >= 2 and bf_prll <= -1:
                p = self.DEL_LRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_prll <= -1:
                p = self.DEL_RRRotation(p)
                reassign_p = True
            elif bf_p <= -2 and bf_prll >= 0:
                p = self.DEL_RLRotation(p)
                reassign_p = True

        # 重新指定小值:p 放中間值: prl 的左邊
        if reassign_p == True:
            prl.left = p
            p.parent = prl

        # 大值: pr 放中間值的右邊
        prl.right = pr
        pr.parent = prl

        # 中間值的右子樹: prlr 放大值: pr 的左邊
        pr.left = prlr

        # 如果中間值的右子樹: prlr 不為 leafnode 再進行下列動作
        reassign_pr = False

        if prlr != self.leafnode:
            prlr.parent = pr

            bf_pr = self.balanceFactor(pr)
            bf_prlr = self.balanceFactor(prlr)

            if bf_pr >= 2 and bf_prlr >= 0:
                pr = self.DEL_LLRotation(pr)
                reassign_pr = True
            elif bf_pr >= 2 and bf_prlr <= -1:
                pr = self.DEL_LRRotation(pr)
                reassign_pr = True
            elif bf_pr <= -2 and bf_prlr <= -1:
                pr = self.DEL_RRRotation(pr)
                reassign_pr = True
            elif bf_pr <= -2 and bf_prlr >= 0:
                pr = self.DEL_RLRotation(pr)
                reassign_pr = True

        # 重新指定大值: pr 放中間值: prl 的右邊
        if reassign_pr:
            prl.right = pr
            pr.parent = prl

        """
            有異動子樹的 Node 都需重新計算高度
            需注意：在下層的 node 需先計算高度
        """
        p.height = self.nodeHeight(p)
        pr.height = self.nodeHeight(pr)
        prl.height = self.nodeHeight(prl)

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(prl)

        return prl

    def noneToLeaf(self, n):
        if n == None:
            return self.leafnode
        return n

    def __fix_insert2(self, n):
        while n.parent.color == Color.RED and n.color == Color.RED:
            parentNode = self.noneToLeaf(n.parent)

            grantParentNode = self.noneToLeaf(parentNode.parent)

            uncleNode = self.leafnode
            if grantParentNode.right == parentNode:
                uncleNode = grantParentNode.left
            else:
                uncleNode = grantParentNode.right

            # re-color
            if parentNode.color == Color.RED and uncleNode.color == Color.RED:
                uncleNode.color = Color.BLACK
                parentNode.color = Color.BLACK
                grantParentNode.color = Color.RED

                # 將 n 指向 grantParentNode 繼續下一個 loop 檢核
                n = grantParentNode

            # rotate
            elif parentNode.color == Color.RED and uncleNode.color == Color.BLACK:
                """
                    用 grantParent、parent node 執行 Balance Factor 檢核,
                    看是否需進行 rotate
                """
                bf_grant_parent = self.balanceFactor(grantParentNode)
                bf_parent = self.balanceFactor(parentNode)

                """
                    以下為符合 rotate 的條件,傳入 grantParentNode 進行 rotate,
                    最後將 n 指向回傳的的中間值 node(因為中間值往上拉),
                    繼續下一個 loop 檢核
                """
                if bf_grant_parent >= 2 and bf_parent >= 1:
                    n = self.LLRotation(grantParentNode)

                elif bf_grant_parent >= 2 and bf_parent <= -1:
                    n = self.LRRotation(grantParentNode)

                elif bf_grant_parent <= -2 and bf_parent <= -1:
                    n = self.RRRotation(grantParentNode)

                elif bf_grant_parent <= -2 and bf_parent >= 1:
                    n = self.RLRotation(grantParentNode)

            if n == self.root:
                break
        # end while loop

        self.root.color = Color.BLACK

        return n

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
                        # 對 k 的 parent 進行 right rotate
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
        newNode.height = 1

        tmpNode = self.root

        # 尋找新節點的 parent
        parentNode = None

        while tmpNode != self.leafnode:
            parentNode = tmpNode
            if key < tmpNode.data:
                # 重新計算 parentNode 的高度
                parentNode.height = self.nodeHeightPlus(
                    parentNode, leftPlus=True)
                tmpNode = tmpNode.left

            elif key > tmpNode.data:
                # 重新計算 parentNode 的高度
                parentNode.height = self.nodeHeightPlus(
                    parentNode, leftPlus=False)
                tmpNode = tmpNode.right

        newNode.parent = parentNode

        # parentNode 為 None, 代表第一次執行 insert, 需指定 root
        if parentNode == None:
            self.root = newNode

        # mew node 為 root, 設定 color: Black 直接 return
        if newNode.parent == None:
            newNode.color = Color.BLACK
            return

        # 指定 newNode 為 parent node 的 left or right
        if key < parentNode.data:
            parentNode.left = newNode
        elif key > parentNode.data:
            parentNode.right = newNode

        # 至少要有 3 個 node 再進行 fix
        if newNode.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert2(newNode)

    """ 尋找左子樹中最大值的 Node"""

    def findLeftSubTreeMaxNode(self, node):
        while node != self.leafnode and node.right != self.leafnode:
            node = node.right
        return node

    """ 尋找右子樹中最小值的 Node"""

    def findRightSubTreeMinNode(self, node):
        while node != self.leafnode and node.left != self.leafnode:
            node = node.left
        return node

    def delete_node(self, n):
        parent_node = self.noneToLeaf(n.parent)

        if parent_node.left == n:
            parent_node.left = self.leafnode
        else:
            parent_node.right = self.leafnode

        # parent 的高度需 loop 上去更新
        self.loop_update_parent_node_height(n)

    def __fix_delete(self, n):

        parent_node = self.noneToLeaf(n.parent)

        # case1 delete node is red
        if n.color == Color.RED:
            # leaf node just delete it
            if n.left == self.leafnode and n.right == self.leafnode:
                self.delete_node(n)

        # delete node is black
        else:
            # 取得 sibling node
            sibling_node = None
            if parent_node.left == n:
                sibling_node = self.noneToLeaf(parent_node.right)
            else:
                sibling_node = self.noneToLeaf(parent_node.left)

            # case3 sibling node is black
            if sibling_node.color == Color.BLACK:
                # case3.1 sibling node's tow children are black
                if sibling_node.left.color == Color.BLACK and sibling_node.right.color == Color.BLACK:
                    # re-color
                    sibling_node.color = Color.RED
                    if parent_node.color == Color.BLACK:
                        parent_node.color = Color.RED
                    else:
                        parent_node.color = Color.BLACK

                    # delete node
                    self.delete_node(n)

                # case3.2 sibling node's any children is RED
                elif sibling_node.left.color == Color.RED or sibling_node.right.color == Color.RED:
                    # delete node
                    self.delete_node(n)

                    """
                        用 parent、sibling node 執行 Balance Factor 檢核,
                        看是否需進行 rotate
                    """
                    bf_parent = self.balanceFactor(parent_node)
                    bf_sibling = self.balanceFactor(sibling_node)

                    if bf_parent >= 2 and bf_sibling >= 0:
                        self.DEL_LLRotation(parent_node)

                    elif bf_parent >= 2 and bf_sibling <= -1:
                        self.DEL_LRRotation(parent_node)

                    elif bf_parent <= -2 and bf_sibling <= -1:
                        self.DEL_RRRotation(parent_node)

                    elif bf_parent <= -2 and bf_sibling >= 0:
                        self.DEL_RLRotation(parent_node)

            # case2 sibling node is red ==> rotation
            else:
                # delete node
                self.delete_node(n)

                """
                    用 parent、sibling node 執行 Balance Factor 檢核,
                    看是否需進行 rotate
                """
                bf_parent = self.balanceFactor(parent_node)
                bf_sibling = self.balanceFactor(sibling_node)

                if bf_parent >= 2 and bf_sibling >= 0:
                    self.DEL_LLRotation(parent_node)

                elif bf_parent >= 2 and bf_sibling <= -1:
                    self.DEL_LRRotation(parent_node)

                elif bf_parent <= -2 and bf_sibling <= -1:
                    self.DEL_RRRotation(parent_node)

                elif bf_parent <= -2 and bf_sibling >= 0:
                    self.DEL_RLRotation(parent_node)

    def delete(self, key):
        delete_node = None

        tmpNode = self.root

        while tmpNode != self.leafnode:
            if key < tmpNode.data:
                tmpNode = tmpNode.left
            elif key > tmpNode.data:
                tmpNode = tmpNode.right
            else:
                delete_node = tmpNode
                break
        # end while loop

        if delete_node is None:
            print(f'Could not find key:{key} in the tree')
            return

        # it's a leaf node
        if delete_node.left == self.leafnode and delete_node.right == self.leafnode:
            self.__fix_delete(delete_node)

        # it has one or two children
        else:
            # 從左子樹中找最大值 or 右子樹的最小值 Node 取代被刪除的 Node
            replace_node = None
            if delete_node.left != self.leafnode:
                replace_node = self.findLeftSubTreeMaxNode(delete_node.left)
            else:
                replace_node = self.findRightSubTreeMinNode(delete_node.right)

            # replace_node 取代其值
            delete_node.data = replace_node.data

            # 刪除 replace_node
            self.__fix_delete(replace_node)


if __name__ == '__main__':

    bst = RedBlackTree()

    bst.insert(70)
    bst.insert(40)
    bst.insert(90)
    bst.insert(20)
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(60)
    bst.pretty_print()

    bst.delete(90)

    bst.pretty_print()
