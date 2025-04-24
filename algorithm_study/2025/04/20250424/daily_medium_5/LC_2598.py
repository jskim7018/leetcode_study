from typing import List
from collections import defaultdict


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = defaultdict(int)

        for num in nums:
            mp[num%value] += 1

        for i in range(len(nums) + 1):
            if mp[i%value] == 0:
                return i
            else:
                mp[i%value] -= 1

        return 0
