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
            self.heapSize = self.heapSize + 1
            return True

        else:
            self.heap[self.heapSize] = newNode
            self.heapSize = self.heapSize + 1

            newIndx = len(self.heap) - 1  # indx 從 0 開始,需減 1
            parentIndx = math.floor((newIndx - 1)/2)

            while parentIndx >= 0 and self.heap[newIndx].priority > self.heap[parentIndx].priority:
                tmp = self.heap[parentIndx]
                self.heap[parentIndx] = self.heap[newIndx]
                self.heap[newIndx] = tmp
                # update index number
                newIndx = parentIndx
                parentIndx = math.floor((newIndx - 1) / 2)

    ''' 進行 maxheap 的修正'''

    def maxHeapify(self, i):
        # 左邊 node 的 indx
        l = i*2 + 1
        # 右邊 node 的 indx
        r = i*2 + 2

        # 比較2個子節點是否比 parent 的 key 值大
        # 因為 heap 的 index 是從 0 開始, 所以 len(self.heap) 需減 1
        if (l <= len(self.heap) - 1) and (self.heap[l].priority > self.heap[i].priority):
            largest = l
        else:
            largest = i

        # 因為 heap 的 index 是從 0 開始, 所以 len(self.heap) 需減 1
        if (r <= len(self.heap) - 1) and self.heap[r].priority > self.heap[largest].priority:
            largest = r

        if i != largest:
            # 進行 swap
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp

            self.maxHeapify(largest)

    def deQueue(self):
        if len(self.heap) == 0:
            return None

        # 取得最後一個 node 的 index
        lastNodeIndx = len(self.heap) - 1

        if len(self.heap) == 1:
            removedNode = self.heap[lastNodeIndx]
            del self.heap[lastNodeIndx]
            return removedNode

        # 將目前第一個 node(priority 最大值) 與最後一個 node switch
        tmpNode = self.heap[0]
        self.heap[0] = self.heap[lastNodeIndx]
        self.heap[lastNodeIndx] = tmpNode

        # 回傳最後一個 node 並刪除
        removedNode = self.heap[lastNodeIndx]
        del self.heap[lastNodeIndx]

        # 對第一個進行 maxHeapify
        self.maxHeapify(0)

        return removedNode

    def display(self):
        count = 0
        for indx in self.heap:
            print(
                f'priority:{self.heap[indx].priority}, element:{self.heap[indx].element}')


if __name__ == "__main__":

    pq = PriorityQueue()

    pq.enQueue(5, 'Leanring')
    pq.enQueue(2, 'Sharing')
    pq.enQueue(7, 'Laughing')
    pq.enQueue(8, 'Playing')
    pq.enQueue(9, 'Seeing')

    pq.display()

    print(f'deQueue node: {pq.deQueue().priority}')
    print(f'deQueue node: {pq.deQueue().priority}')

    print(f'after deQueue')

    pq.display()
