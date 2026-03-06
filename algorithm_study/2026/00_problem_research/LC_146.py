from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.key_cnt = {}
        self.lru_queue = deque()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_queue.appendleft(key)
            self.key_cnt[key] += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            while len(self.cache) == self.capacity:
                popped_k = self.lru_queue.pop()
                self.key_cnt[popped_k] -= 1
                if self.key_cnt[popped_k] == 0:
                    del self.key_cnt[popped_k]
                    del self.cache[popped_k]
        if key not in self.key_cnt:
            self.key_cnt[key] = 0
        self.cache[key] = value
        self.key_cnt[key] += 1
        self.lru_queue.appendleft(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)