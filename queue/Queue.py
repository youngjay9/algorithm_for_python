class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enQueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.length += 1

        return newNode.data

    def deQuque(self):
        if self.first is None:
            return None

        if self.first == self.last:
            self.last = None

        removingNode = self.first
        removingData = removingNode.data

        self.first = removingNode.next
        self.length -= 1
        del removingNode

        return removingData

    def display(self):
        holdNode = self.first
        result = []
        while holdNode is not None:
            result.append(holdNode.data)
            holdNode = holdNode.next

        return result


queue = Queue()

queue.enQueue(5)
queue.enQueue(6)
queue.enQueue(9)

print(f"queue display: {queue.display()}")

print(f"dequeue: {queue.deQuque()}")
print(f"dequeue: {queue.deQuque()}")
print(f"dequeue: {queue.deQuque()}")
print(f"dequeue: {queue.deQuque()}")
print(f"dequeue: {queue.deQuque()}")
