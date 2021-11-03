import math
from typing import Counter, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, priority, element: T):
        self.priority = priority
        self.element = element

class PriorityQueue():
    def __init__(self) -> None:
        self.heap = {}
        self.heapSize = 0

    def enQueue(self, priority, element: T):
        newNode = Node(priority, element)

        if len(self.heap) == 0:
            self.heap[self.heapSize] = newNode
            self.heapSize = self.heapSize +1
            return True    
        
        else:
            self.heap[self.heapSize] = newNode
            self.heapSize = self.heapSize +1

            newIndx = len(self.heap) - 1 # indx 從 0 開始,需減 1
            parentIndx = math.floor((newIndx - 1)/2)

            while parentIndx >=0 and self.heap[newIndx].priority > self.heap[parentIndx].priority:
                tmp = self.heap[parentIndx]
                self.heap[parentIndx] = self.heap[newIndx]
                self.heap[newIndx] = tmp
                # update index number
                newIndx = parentIndx
                parentIndx = math.floor((newIndx - 1) / 2)    
    
    def display(self):
        count = 0
        for indx in self.heap:
            print(f'{self.heap[indx].priority}')


if __name__ == "__main__":
                
    pq = PriorityQueue()

    pq.enQueue(5,'Leanring')
    pq.enQueue(2,'Sharing')
    pq.enQueue(7,'Laughing')
    pq.enQueue(8,'Playing')
    pq.enQueue(8,'Seeing')

    pq.display()





