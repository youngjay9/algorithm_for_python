class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def in_to_out(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.out_stack) == 0:
            self.in_to_out()

        if len(self.out_stack) == 0:
            return None

        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.out_stack) == 0:
            self.in_to_out()

        out_stack_length = len(self.out_stack)

        if out_stack_length == 0:
            return None

        return self.out_stack[out_stack_length-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.out_stack) == 0 and len(self.in_stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":

    q = MyQueue()

    q.push(1)
    q.push(2)

    print(f'pop: {q.pop()}')
    print(f'pop: {q.pop()}')
    print(f'pop: {q.pop()}')
