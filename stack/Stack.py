from linkedlist.DoublyLinkedList import DoublyLinkedList


class Stack:

    def __init__(self):
        self.list = DoublyLinkedList()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        listLength = self.list.length
        popNode = None
        if listLength > 0:
            popNode = self.list.traverseToIndexNode(listLength-1)
            self.list.removeAtIndex(listLength-1)

        return popNode

    def display(self):
        return self.list.display()
