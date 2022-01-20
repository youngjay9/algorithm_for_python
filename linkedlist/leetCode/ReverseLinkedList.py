from typing import Counter, TypeVar, Generic

T = TypeVar("T")


class Node:
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.next = None


class Solution:

    def __init__(self) -> None:
        self.head = None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.head = head

        if head is not None:
            self._reverse(head, head.next)

        return self.head

    def _reverse(self, cur, next):
        if next is not None:
            self._reverse(next, next.next)
            next.next = cur
            cur.next = None
        else:
            self.head = cur


if __name__ == "__main__":
    node1 = Node('1', '1')
    node2 = Node('2', '2')
    node3 = Node('3', '3')
    node4 = Node('4', '4')
    node5 = Node('5', '5')

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    head = solution.reverseList(node1)

    print(f'after reverse head: {head.key}')
