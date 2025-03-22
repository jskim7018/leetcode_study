from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxim = max(nums)

        l = 0
        max_cnt = 0
        ans = 0
        for r in range(n):
            if nums[r] == maxim:
                max_cnt += 1

            while max_cnt == k:
                if nums[l] == maxim:
                    max_cnt -= 1
                l += 1
            ans += l

        return ans
