from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = int(1e9+7)

        ans = 1
        prev_one_idx = -1

        for i in range(n):
            if nums[i] == 1:
                if prev_one_idx > -1:
                    ans *= i-prev_one_idx
                    ans %= MOD
                prev_one_idx = i

        if prev_one_idx == -1:
            return 0
        else:
            return ans
