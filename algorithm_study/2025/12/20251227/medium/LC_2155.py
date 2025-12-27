from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ones_cnt = nums.count(1)
        maxim = 0
        zero_cnt = 0
        curr_ones_cnt = ones_cnt
        for i in range(n+1):
            maxim = max(maxim, zero_cnt + curr_ones_cnt)
            if i < n and nums[i] == 0:
                zero_cnt += 1
            else:
                curr_ones_cnt -= 1

        ans = []
        zero_cnt = 0
        curr_ones_cnt = ones_cnt
        for i in range(n + 1):
            if maxim == zero_cnt + curr_ones_cnt:
                ans.append(i)
            if i < n and nums[i] == 0:
                zero_cnt += 1
            else:
                curr_ones_cnt -= 1

        return ans
