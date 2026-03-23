from sortedcontainers import SortedList


class MRUQueue:

    def __init__(self, n: int):
        self.sorted_list = SortedList()
        self.time = 0
        for i in range(1,n+1):
            self.sorted_list.add((self.time, i))

    def fetch(self, k: int) -> int:
        self.time += 1
        val = self.sorted_list[k-1][1]
        del self.sorted_list[k - 1]
        self.sorted_list.add((self.time, val))
        return val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)