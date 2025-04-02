from typing import List


# TODO: Study the last approach
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n
        for i in range(n):
            prefix_max[i] = nums[i]
            suffix_max[n-i-1] = nums[n-i-1]
            if i > 0:
                prefix_max[i] = max(prefix_max[i], prefix_max[i-1])
                suffix_max[n-i-1] = max(suffix_max[n-i-1], suffix_max[n-i])

        maxim = 0
        for i in range(1, n-1):
            pre_max = prefix_max[i-1]
            suf_max = suffix_max[i+1]
            maxim = max(maxim, (pre_max - nums[i]) * suf_max)

        return maxim
