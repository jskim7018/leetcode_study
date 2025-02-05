from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dq = deque(nums)

        l = 0
        r = len(dq)-1

        ans = 0
        while l<r:
            if dq[l] == dq[r]:
                dq.popleft()
                dq.pop()
                r-=2
            elif dq[l] > dq[r]:
                popped = dq.pop()
                r-=1
                dq[r] += popped
                ans += 1
            else:
                popped = dq.popleft()
                dq[l] += popped
                r-=1
                ans += 1
        return ans
