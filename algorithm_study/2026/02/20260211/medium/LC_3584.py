from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        # sliding window + max,min prefix. max, min suffix
        # TODO: one-pass도 가능. suffix 대신, prefix를 구하면서 오른쪽은 그냥 nums[i] 사용.
        n = len(nums)

        prefix_min = float('inf')
        prefix_max = float('-inf')
        ans = float('-inf')
        for i in range(m-1, n):
            prefix_min = min(prefix_min, nums[i-(m-1)])
            prefix_max = max(prefix_max, nums[i-(m-1)])

            ans = max(ans, prefix_min * nums[i])
            ans = max(ans, prefix_max * nums[i])

        return ans
