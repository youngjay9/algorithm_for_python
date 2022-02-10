from multiprocessing.dummy import current_process
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class Solution():

    def merge(self, l1, l2):
        p1, p2 = l1, l2

        # 設定一個 fake_node 當 merge 過後的 head node
        fake_node = Node(None, None)

        # current 指標
        current_node = fake_node

        while p1 and p2:
            if p1.val <= p2.val:
                current_node.next = p1
                p1 = p1.next
            else:
                current_node.next = p2
                p2 = p2.next

            current_node = current_node.next

        if p1:
            current_node.next = p1
        else:
            current_node.next = p2

        return fake_node.next


if __name__ == "__main__":

    node1 = Node('1', '1')
    node2 = Node('4', '4')
    node3 = Node('5', '5')

    node1.next = node2
    node2.next = node3

    node4 = Node('2', '2')
    node5 = Node('4', '4')
    node6 = Node('6', '6')

    node4.next = node5
    node5.next = node6

    solution = Solution()
    head_node = solution.merge(node1, node4)

    while head_node:
        print(f'{head_node.val}')
        head_node = head_node.next
