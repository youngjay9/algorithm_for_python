import sys, queue, json
from enum import Enum
from types import LambdaType
from typing import Counter, TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, key, element: T):
        self.key = key
        self.element = element
        self.parent = None
        self.left = None
        self.right = None



class LeafNode:
    def __init__(self):
        self.key = 0
        self.element = None
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree():
    def __init__(self):
        self.leafnode = LeafNode()  # 為節省記憶體空間,提供其它 node 預設的 leafNode 都指向同一個
        self.root = self.leafnode
        self.root.parent = self.leafnode
        self.insertLength = 0

    
    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def postOrder(self, currentNode):
        if currentNode is not None:
            self.postOrder(currentNode.left) # L
            self.postOrder(currentNode.right) # R
            print(currentNode.key + " ") # V
            
    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def preOrder(self, currentNode):
        if currentNode is not None:
               print(currentNode.key + "") # V
               self.preOrder(currentNode.left) # L
               self.preOrder(currentNode.right) # R 

    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def inOrder(self, currentNode):
        if currentNode is not None:
            self.inOrder(currentNode.left) # L
            print(currentNode.key)  # V
            self.inOrder(currentNode.right) # R

    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def levelOrder(self, currentNode):
        q = queue.Queue() # 可用於多執行緒的 Queue
        q.put(currentNode)

        while not q.empty():
            
            item = q.get()
            print(f'{item.key} ') # visiting

            # 因為每個 node 有 left 跟 right child, 所以要 if 兩次檢查    
            if item.left is not None:
                q.put(item.left)
            
            if item.right is not None:
                q.put(item.right)
            
    def leftMost(self,currentNode):
        if currentNode is None:
            return currentNode

        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode     

    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def inOrderSuccessor(self, currentNode):
        if currentNode is None:
            return currentNode

        if currentNode.right is not None:
            successorNode = self.leftMost(currentNode.right)
        else:
            successorNode = currentNode.parent
            while successorNode is not None and successorNode.right == currentNode:
                currentNode = currentNode.parent
                successorNode = currentNode.parent

        return 
        
    def rightMost(self, currentNode):
        if currentNode is None:
            return currentNode

        while currentNode.right is not None:
            currentNode = currentNode.right

        return currentNode

    """ 參考 folder algorithm_datastructure/2_BinaryTree_Traversal """
    def inOrderPredecessor(self, currentNode):
        if currentNode is None:
            return currentNode

        if currentNode.left is not None:
            predecessorNode = self.rightMost(currentNode.left)
        else:
            predecessorNode = currentNode.parent
            while predecessorNode is not None and predecessorNode.left == currentNode:
                currentNode = currentNode.parent
                predecessorNode = currentNode.parent    

        return predecessorNode

    
    def getNextInsertElement(self, str):
        print(f'insert len:{self.insertLength} len: {len(str)}')
        # 用 insertLength 控管 index 到哪個字元, 避免超過字串長度
        if self.insertLength == len(str):
            return None

        data = str[self.insertLength]

        self.insertLength = self.insertLength +1
        
        return data

    
    """ 使用 level order 搭配 Queue 的方式建立 Tree """
    def createTree(self, str):
        # 用 index 的方式一個一個取元素
        data = self.getNextInsertElement(str)

        # 指定 root
        self.root = Node(data, data)

        # 將root先放進 queue
        q = queue.Queue() # 可用於多執行緒的 Queue
        q.put(self.root)

        while not q.empty() and data is not None:
            
            currentNode = q.get()

            """ 
                因為是 Binary tree, 在迴圈中需一次讀取 2 個新增元素(getNextInsertElement),
                一個給 left, 一個給 right
            """
            # current的leftchild
            data = self.getNextInsertElement(str)
            if data is None:
                continue
            if data != 'x':
                newNode = Node(data, data)
                newNode.parent = currentNode
                currentNode.left = newNode
                q.put(newNode)

            # current的rightchild  
            data = self.getNextInsertElement(str)
            if data is None:
                continue
            if data != 'x': 
                newNode = Node(data, data)
                newNode.parent = currentNode
                currentNode.right = newNode
                q.put(newNode)

            



                          

if __name__ == "__main__":

    # insert 的字串(x 代表不新增,跳過)
    str = "ABCDEFxxxGHxI"
    bt = BinaryTree()
    bt.createTree(str)

    # 使用 level order 列印出 Binarytree 排序後的結果
    bt.levelOrder(bt.root)

    # inOrderSuccessor = bt.inOrderSuccessor(nodeA)

    # if inOrderSuccessor is not None:    
    #     print(f"inOrderSuccessor :{inOrderSuccessor.key}")

    # inOrderPrecessor = bt.inOrderPredecessor(nodeF)

    # if inOrderPrecessor is not None:
    #     print(f"inOrderPrecessor :{inOrderPrecessor.key}")    
    
    # bt.levelOrder(nodeA)
   
    
