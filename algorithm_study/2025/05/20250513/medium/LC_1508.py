from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = int(1e9+7)
        subarray_sums = []
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                subarray_sums.append(sum_)

        subarray_sums.sort()
        ans = 0
        for i in range(left-1, right):
            ans += subarray_sums[i]
            ans %= MOD

        return ans
