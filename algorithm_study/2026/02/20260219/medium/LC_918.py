from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # suffix max 배열 준비해 둠.
        # 중간 일때와, 1개일때 max 구함.
        # prefix max, suffix max 동적으로 더해서 중간아닐때 max 구함.

        # 1개일때와 중간 일때 구함.

        # TODO: kadane로 간단히 가능. max를 구하면 중간의 max, min을 구해서 빼면 양끝 max를 구하는 것 과 같음.
        maxim = max(nums)
        curr = 0
        for num in nums:
            curr += num
            if curr < 0:
                curr = 0
            else:
                maxim = max(maxim, curr)

        # 양끝일 경우
        n = len(nums)
        suffix_sum_max = [0] * n
        suffix_sum = 0
        for i in range(n-1, -1, -1):
            suffix_sum += nums[i]
            suffix_sum_max[i] = suffix_sum
            if i+1 < n:
                suffix_sum_max[i] = max(suffix_sum_max[i], suffix_sum_max[i+1])

        prefix_sum_max = float('-inf')
        curr_prefix_sum = 0
        for i in range(n):
            maxim = max(maxim, prefix_sum_max + suffix_sum_max[i])
            curr_prefix_sum += nums[i]
            prefix_sum_max = max(curr_prefix_sum, prefix_sum_max)

        return maxim
