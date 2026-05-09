class ListNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map<key, ListNode>
        
        # 使用 Dummy Head 和 Dummy Tail 避免處理邊界 null check
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 # 題目要求
        
        node = self.cache[key]
        self._move_to_front(node) # 讀取過也要變更活躍度
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Case 1: Key 存在 -> 更新值 + 移到最前
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            # Case 2: Key 不存在 -> 插入新節點
            node = ListNode(key=key, val=value)
            self.cache[key] = node
            self._insert_to_front(node)
            
            # 檢查容量
            if len(self.cache) > self.capacity:
                # 刪除最後一個真實節點 (tail.prev)
                lru_node = self.tail.prev
                self._delete_node(lru_node)
                del self.cache[lru_node.key] # 記得從 map 移除
    
    def _delete_node(self, node):
        # 雙向鏈表標準刪除：把前後接起來，跳過 node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_to_front(self, node):
        # 插入到 head 和 head.next 之間
        # 1. 設定 node 的指針
        node.prev = self.head
        node.next = self.head.next
        
        # 2. 設定前後節點的指針指向 node
        self.head.next.prev = node # 這一行最容易忘！
        self.head.next = node

    def _move_to_front(self, node):
        # 組合技：先刪除，再插入到最前
        self._delete_node(node)
        self._insert_to_front(node)