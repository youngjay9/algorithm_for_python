import sys
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

    def __init__(self, rootNode):
        self.root = rootNode    

    def postOrder(self, currentNode):
        if currentNode is not None:
            self.postOrder(currentNode.left) # L
            self.postOrder(currentNode.right) # R
            sys.stdout.write(currentNode.key + " ") # V
            
    def preOrder(self, currentNode):
        if currentNode is not None:
               sys.stdout.write(currentNode.key + "") # V
               self.preOrder(currentNode.left) # L
               self.preOrder(currentNode.right) # R 

    def inOrder(self, currentNode):
        if currentNode is not None:
            self.inOrder(currentNode.left) # L
            sys.stdout.write(currentNode.key)  # V
            self.inOrder(currentNode.right) # R

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
         
    nodeB.left = nodeD
    nodeB.right = nodeE

    nodeC.left = nodeF

    nodeE.left = nodeG
    nodeE.right = nodeH

    nodeF.right = nodeI

    bt = BinaryTree(nodeA)

     # bt.postOrder(nodeA)

    # bt.preOrder(nodeA)

    bt.inOrder(nodeA)
    
    
