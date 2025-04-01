from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)

        for i, val in enumerate(nums):
            mp[val].append(i)

        ans = [0] * len(nums)
        for lst in mp.values():
            initial = sum(lst)+len(lst)
            left_cnt = 0
            right_cnt = len(lst)
            prev = -1
            for v in lst:
                diff = v-prev
                initial -= diff * right_cnt
                initial += diff * left_cnt
                left_cnt += 1
                right_cnt -= 1
                prev = v
                ans[v] = initial

        return ans
