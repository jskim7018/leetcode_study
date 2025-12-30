from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)

        maxim = 0
        for num in nums:
            maxim |= num

        ans = 0

        def brute_force(curr: int, idx: int):
            nonlocal ans

            if idx >= n:
                if curr == maxim:
                    ans += 1
                return

            brute_force(curr, idx + 1)
            brute_force(curr | nums[idx], idx + 1)

        brute_force(0, 0)

        return ans
