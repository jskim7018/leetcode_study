from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum_ = sum(nums)

        ans = target//sum_ * n

        target %= sum_
        if target == 0:
            return ans

        prefix_sum = [0] * (len(nums)*2)

        mp = dict()

        minim_len = float('inf')
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)*2):
            arr_i = i%n
            prefix_sum[i] += nums[arr_i] + prefix_sum[i-1]
            need = prefix_sum[i] - target
            if need in mp:
                minim_len = min(minim_len, i-mp[need])
            mp[prefix_sum[i]] = i
        ans += minim_len
        if ans == float('inf'):
            return -1
        else:
            return ans
