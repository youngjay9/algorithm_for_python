from linkedlist.DoublyLinkedList import DoublyLinkedList


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
        else:
            holdNode = self.top
            self.top = newNode
            self.top.next = holdNode

        self.length += 1

        return newNode.data

    def pop(self):
        if self.top is None:
            return None

        popNode = self.top
        popData = popNode.data

        self.top = popNode.next
        self.length -= 1
        del popNode

        return popData

    def display(self):
        holdNode = self.top
        result = []
        while holdNode is not None:
            result.append(holdNode.data)
            holdNode = holdNode.next

        return result
