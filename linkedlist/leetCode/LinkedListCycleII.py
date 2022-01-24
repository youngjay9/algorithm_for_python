from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.next = None


class LinkedListCycleII:

    def detectCycle(self, head):
        # 用 HashMap 存放找過的 node
        items = {}
        items[head.val] = head

        next_node = head.next

        while next_node:
            if next_node.val in items.keys():
                return items[next_node.val]

            items[next_node.val] = next_node

            next_node = next_node.next
        return None


if __name__ == "__main__":

    node3 = Node('3', '3')
    node2 = Node('2', '2')
    node0 = Node('0', '0')
    node4 = Node('-4', '-4')

    node3.next = node2
    node2.next = node0
    node0.next = node4
    node4.next = node2

    l = LinkedListCycleII()
    node = l.detectCycle(node3)
    print(f'node: {node.val}')
