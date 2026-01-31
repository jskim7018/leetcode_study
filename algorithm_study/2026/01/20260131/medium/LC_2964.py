from typing import List
from collections import defaultdict


class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        rem_cnt = defaultdict(int)
        n = len(nums)

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                need = (d - ((nums[i]+nums[j]) % d)) % d
                ans += rem_cnt[need]
            rem_cnt[nums[i] % d] += 1
        return ans
