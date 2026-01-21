from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_min = list(nums)

        for i in range(n):
            if i-1 >= 0:
                prefix_min[i] = min(prefix_min[i], prefix_min[i-1])

        suffix_min = nums[-1]
        ans = float('inf')
        for i in range(n-2, 0, -1):
            if prefix_min[i-1] < nums[i] and suffix_min <nums[i]:
                ans = min(ans, prefix_min[i-1] + nums[i] + suffix_min)
            suffix_min = min(suffix_min, nums[i])

        if ans == float('inf'):
            return -1
        else:
            return ans
