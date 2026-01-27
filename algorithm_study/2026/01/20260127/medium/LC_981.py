from collections import defaultdict
from bisect import bisect_left


class TimeMap:

    def __init__(self):
        self.key_to_vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_vals[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_left(self.key_to_vals[key], (timestamp+1, ''))-1
        if idx == -1:
            return ""
        else:
            return self.key_to_vals[key][idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)