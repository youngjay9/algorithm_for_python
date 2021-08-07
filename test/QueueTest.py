import threading, queue
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


def leftMost(current):
    
    while current.left is not None:
        current = current.left    

    return current

def levelOrder(currentNode):
    q = queue.Queue() # 可用於多執行緒的 Queue
    q.put(currentNode)

    while not q.empty():
        
        item = q.get()
        print(f'{item.key} ') # visiting

        if item.left is not None:
            q.put(item.left)
        
        if item.right is not None:
            q.put(item.right)     

if __name__ == "__main__":
    q = queue.Queue()
    if not q.empty():
        q.get()

    
        

    
