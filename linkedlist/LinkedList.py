from linkedlist.Node import Node


class LinkedList:
    """
        init 初始化 head 指向 linkedlist 的第一個元素，
        tail 指向 linkedlist 的最後一個元素
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """將新元素加在 linkedlist 最後方"""

    def append(self, value):
        node = Node(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

        return self

    """將新元素加在 linkedlist head 的前方"""

    def prepend(self, value):
        if self.head is None and self.tail is None:
            return self.append(value)

        node = Node(value)

        node.next = self.head

        self.head = node

        self.length += 1

        return self

    def traverseToIndexNode(self, index):
        currenNode = self.head
        i = 0

        while currenNode is not None and i < index:
            i += 1
            currenNode = currenNode.next

        return currenNode

    """ 將元素新增在指定的 index """

    def insertAtIndex(self, index, value):
        # 需注意以下 index 的處理
        if index is 0:
            self.prepend(value)
            return self.display()

        elif index >= self.length:
            self.append(value)
            return self.display()

        # 走尋到 (index-1) 的元素，再插入新元素
        holdNode = self.traverseToIndexNode(index-1)

        newNode = Node(value)
        newNode.next = holdNode.next
        holdNode.next = newNode
        self.length += 1

        return self.display()

    def removeAtIndex(self, index):
        # 走尋到 (index-1) 的元素
        holdNode = self.traverseToIndexNode(index-1)
        removingNode = holdNode.next

        holdNode.next = removingNode.next

        del removingNode

        self.length -= 1

        return self.display()

    def display(self):
        result = []
        ptr = self.head
        while ptr is not None:
            result.append(ptr.data)
            ptr = ptr.next
        return result
