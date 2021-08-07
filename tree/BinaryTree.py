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

    
    def postOrder(self, currentNode):
        if currentNode is not None:
            self.postOrder(currentNode.left) # L
            self.postOrder(currentNode.right) # R
            print(currentNode.key + " ") # V
            
    def preOrder(self, currentNode):
        if currentNode is not None:
               print(currentNode.key + "") # V
               self.preOrder(currentNode.left) # L
               self.preOrder(currentNode.right) # R 

    def inOrder(self, currentNode):
        if currentNode is not None:
            self.inOrder(currentNode.left) # L
            print(currentNode.key)  # V
            self.inOrder(currentNode.right) # R

    def levelOrder(self, currentNode):
        q = queue.Queue() # 可用於多執行緒的 Queue
        q.put(currentNode)

        while not q.empty():
            
            item = q.get()
            print(f'{item.key} ') # visiting

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
        if self.insertLength == len(str) -1:
            return None

        self.insertLength = self.insertLength +1
        data = str[self.insertLength]

        return data

    def createTree(self, str):

        q = queue.Queue() # 可用於多執行緒的 Queue
        
        self.root = Node(str[self.insertLength], str[self.insertLength])

        self.insertLength = self.insertLength +1
        data = str[self.insertLength]

        currentNode = self.root    

        # 使用 levelOrder 的方式建立
        while data is not None:
            if data != 'x': # current的leftchild
                newNode = Node(data, data)
                newNode.parent = currentNode
                currentNode.left = newNode
                q.put(newNode)

            data = self.getNextInsertElement(str)

            if data != 'x': # current的rightchild
                newNode = Node(data, data)
                newNode.parent = currentNode
                currentNode.right = newNode
                q.put(newNode)

            currentNode = q.get()

            data = self.getNextInsertElement(str)



                          

if __name__ == "__main__":

    nodeA = Node("A", "A")
    nodeB = Node("B", "B")
    nodeC = Node("C", "C")
    nodeD = Node("D", "D")
    nodeE = Node("E", "E")
    nodeF = Node("F", "F")
    nodeG = Node("G", "G")
    nodeH = Node("H", "H")
    nodeI = Node("I", "I")
    
    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.parent = nodeA
    nodeC.parent = nodeA
         
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeD.parent = nodeB
    nodeE.parent = nodeB

    nodeC.left = nodeF
    nodeF.parent = nodeC

    nodeE.left = nodeG
    nodeE.right = nodeH
    nodeG.parent = nodeE
    nodeH.parent = nodeE

    nodeF.right = nodeI
    nodeI.parent = nodeF

    # bt = BinaryTree(nodeA)

     # bt.postOrder(nodeA)

    # bt.preOrder(nodeA)

    # bt.inOrder(nodeA)

    # inOrderSuccessor = bt.inOrderSuccessor(nodeA)

    # if inOrderSuccessor is not None:    
    #     print(f"inOrderSuccessor :{inOrderSuccessor.key}")

    # inOrderPrecessor = bt.inOrderPredecessor(nodeF)

    # if inOrderPrecessor is not None:
    #     print(f"inOrderPrecessor :{inOrderPrecessor.key}")    
    
    # bt.levelOrder(nodeA)
   
    # insert 的字串
    str = "ABCDEFxxxGHxI"
    bt = BinaryTree()
    bt.createTree(str)

    bt.levelOrder(bt.root)
