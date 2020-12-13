from linkedlist.Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """將新元素加在 linkedlist 最後方"""

    def append(self, value):
        newNode = Node(value)

        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail = newNode
            newNode.prev = self.tail
            self.tail = newNode

        return self

    def prepend(self, value):
        if self.head is None and self.tail is None:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        return self

    def insertAtIndex(self, index, value):
        pass

    def traverseToIndexNode(self, index):

        if index <= 0:
            return self.head

        currenNode = self.head
        i = 0

        while currenNode is not None and i < index:
            i += 1
            currenNode = currenNode.next

        return currenNode

    def display(self):
        result = []
        ptr = self.head
        while ptr is not None:
            result.append(ptr.data)
            ptr = ptr.next
        return result
