from typing import List
from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        ans = []
        for k,v in counter.items():
            for i in range(v):
                if i >= len(ans):
                    ans.append([])
                ans[i].append(k)
        return ans
