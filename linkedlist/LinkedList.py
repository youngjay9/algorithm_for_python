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

    """移動到指定 index 的 Node"""

    def traverseToIndexNode(self, index):

        if index <= 0:
            return self.head

        currenNode = self.head
        i = 0

        while currenNode is not None and i < index:
            i += 1
            currenNode = currenNode.next

        return currenNode

    """ 將元素新增在指定的 index """

    def insertAtIndex(self, index, value):
        # 需注意以下 index 的處理
        if index == 0:
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

        print(f"holdNode: {holdNode.data}")
        print(f"removingNode: {removingNode.data}")

        holdNode.next = removingNode.next

        del removingNode

        self.length -= 1

        return self.display()

    """透過 recursive 的機制進行 reverse, 可看 stack 執行過程的圖示"""

    def reverse(self, prev, next):

        if next is not None:
            print(f"prev: {prev.data}, next:{next.data}")
            self.reverse(next, next.next)
            next.next = prev
            # 一直指定 tail 的 Node
            self.tail = prev
            self.tail.next = None
            print(f"r_tail:{self.tail.data}")
        else:
            self.head = prev

    def display(self):
        result = []
        ptr = self.head
        while ptr is not None:
            result.append(ptr.data)
            ptr = ptr.next
        return result
