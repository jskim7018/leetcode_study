from typing import List
import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        prefix_sum = [0] * n

        nums.sort()
        for i in range(n):
            prefix_sum[i] = nums[i]

            if i-1 >= 0:
                prefix_sum[i] += prefix_sum[i-1]
        ans = []
        for q in queries:
            left = bisect.bisect_left(nums, q)-1
            right = bisect.bisect_right(nums, q)

            need = 0
            if left >= 0:
                need += q*(left+1) - prefix_sum[left]
            if right < n:
                need += (prefix_sum[n-1] - q*(n-right))
                if right-1 >= 0:
                    need -= prefix_sum[right-1]
            ans.append(need)

        return ans
