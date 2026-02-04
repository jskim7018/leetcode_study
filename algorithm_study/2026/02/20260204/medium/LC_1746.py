from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        # suffix max 만들어둠.
        # 답 구하면서 prefix max 만들고 max 경신하면서 답을 구함.
        n = len(nums)
        suffix_max = [0] * n
        for i in range(n-1, -1, -1):
            suffix_max[i] = max(0, nums[i])
            if i+1 < n:
                suffix_max[i] = max(suffix_max[i], nums[i]+suffix_max[i+1])

        prefix_max = 0
        ans = float('-inf')
        for i in range(n):
            _sum = nums[i]*nums[i]
            if i-1 >= 0:
                _sum += prefix_max
            if i+1 < n:
                _sum += suffix_max[i+1]

            prefix_max = max(0, prefix_max + nums[i])
            ans = max(ans, _sum)
        return ans
