from typing import List
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            if i >= 1:
                nums[i] += nums[i - 1]
            nums[i] %= k
            if nums[i] < 0:
                nums[i] = (nums[i]+k)%k

        counter = Counter(nums)
        ans = 0
        counter[0] += 1
        for v in counter.values():
            ans += (v*(v-1))//2
        return ans
