from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            set_even = set()
            set_odd = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    set_even.add(nums[j])
                else:
                    set_odd.add(nums[j])
                if len(set_even) == len(set_odd):
                    ans = max(ans, j - i + 1)

        return ans
