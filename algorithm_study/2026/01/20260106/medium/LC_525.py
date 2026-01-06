from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        sum_first_idx = dict()
        sum_first_idx[0] = -1

        accum = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                accum += -1
            else:
                accum += 1
            if accum in sum_first_idx:
                ans = max(ans, i-sum_first_idx[accum])
            else:
                sum_first_idx[accum] = i

        return ans
