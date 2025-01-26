from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()

        cnt = 1
        curr = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] == curr+1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            curr = nums[i]
        ans = max(ans, cnt)

        return ans
