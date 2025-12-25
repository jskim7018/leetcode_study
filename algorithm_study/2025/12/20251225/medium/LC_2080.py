from typing import List
from collections import defaultdict
import bisect


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.num_to_indexes = defaultdict(list)
        for i, num in enumerate(arr):
            self.num_to_indexes[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        idx_list = self.num_to_indexes[value]
        l = bisect.bisect_left(idx_list, left)
        r = bisect.bisect_right(idx_list, right) - 1

        return max(0, r-l+1)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)