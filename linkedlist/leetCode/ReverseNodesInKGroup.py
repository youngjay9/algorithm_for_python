from audioop import reverse
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.next = None


class Solution:

    def __init__(self):
        self.first_node = None

    """進行 k group 的 reverse"""

    def reverse(self, cur_node, next_node, count):
        if count is (self.k)-1:
            return

        count += 1
        self.reverse(next_node, next_node.next, count)
        next_node.next = cur_node

        return cur_node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 讓 reverse function 得知 k
        self.k = k
        # point 每個 k group 的第一個 node, reverse 的起點
        k_first_node = head
        # point to linkedList every nodes
        next_node = head
        # 計數每個 k group
        count = 0

        first_time_reverse = True

        while next_node:
            if count is (k-1):
                # 先暫存 reverse k group 的起點 node
                reverse_start_node = k_first_node
                # 指向下一個 k group 的起點
                k_first_node = next_node.next

                # 第一次執行 reverse, 先指定要回傳的第一個 node
                if first_time_reverse:
                    self.first_node = next_node
                    first_time_reverse = False
                # 第二次執行 reverse 時,指定上一次 reverse 與此次 reverse 的連結
                else:
                    if prev_node:
                        prev_node.next = next_node

                # 開始進行 k group 的 reverse, 並回傳此次 reverse 後的最後一個 node, 為下一次 reverse 做連結
                prev_node = self.reverse(
                    reverse_start_node, reverse_start_node.next, 0)

                # reverse 後重新指定下一個連結
                reverse_start_node.next = k_first_node

                # count 歸零,重新計數 k group
                count = 0
                # reassign next_node
                next_node = k_first_node

                continue

            count += 1
            next_node = next_node.next

        return self.first_node


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
    head_node = solution.reverseKGroup(node1, 2)
    print(f'head: {head_node.key}')
