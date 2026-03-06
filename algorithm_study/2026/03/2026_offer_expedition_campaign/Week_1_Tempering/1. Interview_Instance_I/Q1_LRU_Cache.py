import heapq


# TODO: Doubly Linked List를 사용하면 O(1)이 가능.
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.timestamps = {}
        self.curr_time = 0
        self.min_time_heap = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.curr_time += 1
            self.timestamps[key] = self.curr_time
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.curr_time += 1
        if key not in self.cache:
            while len(self.min_time_heap) == self.capacity:
                t, k = heapq.heappop(self.min_time_heap)
                if self.timestamps[k] != t:
                    heapq.heappush(self.min_time_heap, (self.timestamps[k], k))
                else:
                    del self.timestamps[k]
                    del self.cache[k]
                    break
            heapq.heappush(self.min_time_heap, (self.curr_time, key))
        self.timestamps[key] = self.curr_time
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)