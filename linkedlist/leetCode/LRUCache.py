from typing import Counter, TypeVar, Generic

T = TypeVar("T")


class Node(object):
    def __init__(self, key, val: T):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.items = {}  # 用來存放 key 對應的 Node, 這樣就不用花 O(n) 的時間搜尋key 對應的 Node

    '''將 cur_node 移至鏈表頭部'''

    def move_cur_node_to_haed(self, cur_node):
        cur_node.next = self.head
        self.head.prev = cur_node
        self.head = cur_node

    def put(self, key, val: T):
        # key 不存在, 將新增的 Node 新增至鏈表頭部
        if key not in self.items.keys():
            newNode = Node(key, val)
            self.items[key] = newNode
            # 第一次新增 Node, 指定 head 跟 tail
            if self.head is None and self.tail is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.move_cur_node_to_haed(newNode)
            # 新增 Node 以後, 超過鏈表的長度需將 tail Node 刪除,以維護 capacity
            if len(self.items) > self.capacity:
                tail_node = self.tail
                # 將 items 對應的 tail_node.key 刪除
                self.items.pop(tail_node.key)
                # 變更 tail 指標
                self.tail = tail_node.prev
                self.tail.next = None
                del tail_node
        # key 存在, 根據 node 為 head、tail、others 做以下變更
        else:
            cur_node = self.items[key]
            cur_node.val = val
            # 該 node 為 head 只要直接設定 node.val 即可
            # 該 Node 為 tail
            if cur_node is self.tail:
                # 變更 tail 指標
                self.tail = cur_node.prev
                self.tail.next = None
                # 將 cur_node 移至鏈表頭部
                self.move_cur_node_to_haed(cur_node)
            # 該 node 不為 head 也不為 tail
            elif cur_node is not self.head:
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                # 將 cur_node 移至鏈表頭部
                self.move_cur_node_to_haed(cur_node)

    '''
      key 對應的 node 為: 
      1. head, 則直接回傳 node.val
      2. tail, 變更 tail 指標, 並將 node 移至鏈表頭部
      3. others, 將 node 從原本位置刪除,並移至鏈表頭部
    '''

    def get(self, key):
        if key in self.items.keys():
            cur_node = self.items[key]
            # 該 Node 為 tail
            if cur_node is self.tail:
                # 如果 cur_node tail node, 則變更 tail 指摽指向 cur_node.prev
                self.tail = cur_node.prev
                self.tail.next = None
                # 將 cur_node 移至鏈表頭部
                self.move_cur_node_to_haed(cur_node)
            # 該 node 不為 head 也不為 tail
            elif cur_node is not self.head:
                # 將 cur_node 從原本位置刪除
                prev_node = cur_node.prev
                next_node = cur_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                # 將 cur_node 移至鏈表頭部
                self.move_cur_node_to_haed(cur_node)

            return cur_node.val
        else:
            return -1

    def __repr__(self):
        result = []
        cur_node = self.head
        while cur_node is not None:
            result.append(str(cur_node.val))
            cur_node = cur_node.next
        return '->'.join(result)


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put('30', 'curry')
    lru_cache.put('23', 'Green')
    lru_cache.put('0', 'Payton')
    print(lru_cache)

    print(f"get(0): {lru_cache.get('0')}")
    print(lru_cache)

    print(f"get(30): {lru_cache.get('30')}")
    print(lru_cache)

    print(f"get(0): {lru_cache.get('0')}")
    print(lru_cache)

    print(f"put(11): {lru_cache.put('11','Thompson')}")
    print(lru_cache)

    print(f"{lru_cache.put('0','Arenas')}")
    print(lru_cache)

    print(f"{lru_cache.put('30','Wallace')}")
    print(lru_cache)
