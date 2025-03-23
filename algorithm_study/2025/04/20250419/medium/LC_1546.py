from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i-1]

        mp = dict()
        mp[0] = -1
        ans = 0

        left_bound = -1
        for i in range(n):
            need_remove = nums[i] - target
            if need_remove in mp:
                if mp[need_remove] >= left_bound:
                    ans += 1
                    left_bound = i
            mp[nums[i]] = i

        return ans
