from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.next = None


class SwapTwoPairNode:

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._swap(head)

    def _swap(self, cur_node):

        if not cur_node or not cur_node.next:
            return cur_node

        next_node = cur_node.next

        cur_node.next = self._swap(next_node.next)

        next_node.next = cur_node

        return next_node


if __name__ == "__main__":

    node1 = Node('1', '1')
    node2 = Node('2', '2')
    node3 = Node('3', '3')
    node4 = Node('4', '4')

    node1.next = node2
    node2.next = node3
    node3.next = node4

    swapTwoPairNode = SwapTwoPairNode()
    head_node = swapTwoPairNode.swapPairs(node1)

    tmp_node = head_node

    while tmp_node:
        print(f'tmp_node: {tmp_node.key}')
        tmp_node = tmp_node.next
