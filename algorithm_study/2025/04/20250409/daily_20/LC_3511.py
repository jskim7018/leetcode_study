from typing import List


class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        curr_sum = 0
        i = 2
        while i < n:
            # use lesser of currently accumulated sum or just nums[i-2]
            if curr_sum + nums[i-2] >= nums[i-2]:
                curr_sum = nums[i-2]
            else:
                curr_sum += nums[i - 2]

            # if adding last 2 and curr_sum (accumulated or num[i-2]) is lesser than negative, replace nums[i] as 1e18
            if nums[i] + nums[i-1] + curr_sum <= 0:
                nums[i] = 1e18
                ans += 1
                curr_sum = 0
                i += 2
            i += 1

        return ans
