import sys, queue, json, math
from enum import Enum
from types import LambdaType
from typing import Counter, TypeVar, Generic


T = TypeVar("T")

class HeapNode(Generic[T]):
    def __init__(self, key, element: T):
        self.key = key
        self.element = element
        
class BinaryHeap():
    def __init__(self) -> None:
        self.heap = {}
        self.heapSize = 0

    
    def buildMaxHeap(self, array):
        # 將 insert element 放進 heap ditionary
        for i in range(len(array)):
            self.heap[i] = array[i]

        # heap ditionary 的 index 是從 0 開始,所以需 length - 1 
        self.heapSize = len(self.heap) -1

        '''
            i從 0 開始,找尋有 2 個 child 的 node,
            也就是 heap ditionary 的 index 從 0 到 math.floor(heapSize) 的 node
        ''' 
        count = math.floor(self.heapSize)
        while count >=0:
            print(f'i: {count}')
            self.maxHeapify(count)
            count = count -1    

        print(self.heap)
 



            
    def maxHeapify(self, i):
        l = i*2 +1
        r = i*2 +2

        # 比較2個子節點是否比 parent 的 key 值大
        if l<= self.heapSize and self.heap[l].key > self.heap[i].key:
            largest = l
        else:
            largest = i

        if r<= self.heapSize and self.heap[r].key >self.heap[largest].key:
            largest = r

        if i!= largest:
            # 進行 swap
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp

            self.maxHeapify(largest)


if __name__ == "__main__":
    length = 0
    insertElementArray = {}

    node1 = HeapNode('15', 'D')
    insertElementArray[length] = node1
    length = length +1

    node2 = HeapNode('3', 'A')
    insertElementArray[length] = node2
    length = length +1

    node3 = HeapNode('17', 'F')
    insertElementArray[length] = node3
    length = length +1

    node4 = HeapNode('18', 'G')
    insertElementArray[length] = node4
    length = length +1

    node5 = HeapNode('20', 'H')
    insertElementArray[length] = node5
    length = length +1

    node6 = HeapNode('2', 'E')
    insertElementArray[length] = node6
    length = length +1

    node7 = HeapNode('1', 'I')
    insertElementArray[length] = node7
    length = length +1

    node8 = HeapNode('666', 'B')
    insertElementArray[length] = node8
    length = length +1

    


    binaryHeap = BinaryHeap()
    binaryHeap.buildMaxHeap(insertElementArray)