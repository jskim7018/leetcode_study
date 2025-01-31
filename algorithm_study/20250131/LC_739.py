from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = deque()

        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stck) != 0 and stck[-1][0] < temperatures[i]:
                v, idx = stck.pop()
                ans[idx] = i-idx
            stck.append((temperatures[i], i))

        return ans
