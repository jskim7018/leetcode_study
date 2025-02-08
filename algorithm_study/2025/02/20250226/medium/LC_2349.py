import heapq

class NumberContainers:

    def __init__(self):
        self.idx_number_mp = {}
        self.number_idx_mp = {}

    def change(self, index: int, number: int) -> None:
        self.idx_number_mp[index] = number
        if number in self.number_idx_mp:
            heapq.heappush(self.number_idx_mp[number], index)
        else:
            self.number_idx_mp[number] = [index]
            heapq.heapify(self.number_idx_mp[number])

    def find(self, number: int) -> int:
        if number not in self.number_idx_mp.keys():
            return -1
        else:
            while self.number_idx_mp[number]:
                idx_to_ret = self.number_idx_mp[number][0]
                if idx_to_ret in self.idx_number_mp.keys() and self.idx_number_mp[idx_to_ret] == number:
                    return idx_to_ret
                else:
                    heapq.heappop(self.number_idx_mp[number])
            return -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)