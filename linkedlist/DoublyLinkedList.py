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
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1

        return self

    def prepend(self, value):
        if self.head is None and self.tail is None:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

        return self

    """ 將元素新增在指定的 index """

    def insertAtIndex(self, index, value):
        # 需注意以下 index 的處理
        if index == 0:
            self.prepend(value)
            return self.display()

        elif index >= self.length - 1:
            self.append(value)
            return self.display()

        holdNode = self.traverseToIndexNode(index-1)
        nextNode = holdNode.next
        newNode = Node(value)

        holdNode.next = newNode

        newNode.prev = holdNode
        newNode.next = nextNode

        nextNode.prev = newNode

        self.length += 1

        return self.display()

    def removeAtIndex(self, index):

        if self.length == 0:
            return self.display()

        removingNode = None

        if index == 0:
            removingNode = self.head
            if removingNode.next is not None:
                self.head = removingNode.next
                self.head.prev = None

        elif index >= (self.length - 1):
            removingNode = self.tail
            if removingNode.prev is not None:
                self.tail = removingNode.prev
                self.tail.next = None

        else:
            holdNode = self.traverseToIndexNode(index-1)
            removingNode = holdNode.next
            nextNode = removingNode.next
            holdNode.next = nextNode
            nextNode.prev = holdNode

        self.length -= 1
        del removingNode

        if self.length == 0:
            self.head = None
            self.tail = None

        return self.display()

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
