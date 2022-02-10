
from platform import node
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class MergeSortLinkedList():

    '''不要用 recursive 的方式會比較省記憶體空間'''

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

    """取得 LinkedList 的中間節點"""

    def getMiddleNode(self, head):
        if not head:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    m = MergeSortLinkedList()
    node1 = Node('1', '1')
    node2 = Node('3', '3')
    node3 = Node('4', '4')
    node4 = Node('2', '2')
    node5 = Node('6', '6')
    node6 = Node('5', '5')

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    middle = m.getMiddleNode(node1)
    print(f'{middle.key}')
