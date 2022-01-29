import collections
from inspect import stack


class MyStack(object):
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.queue1:
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())

    def pop(self):
        """
        :rtype: int
        """
        if self.queue1:
            return self.queue1.popleft()
        else:
            return self.queue2.popleft()

    def top(self):
        """
        :rtype: int
        """
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1 and not self.queue2


if __name__ == "__main__":

    stack = MyStack()

    stack.push(1)
    stack.push(2)

    print(f'{stack.pop()}')
    print(f'{stack.pop()}')
