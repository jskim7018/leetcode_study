from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # sweeping 가능.
        # TODO: sliding window로 정렬 후 공통 범위 까지 구하고 window max길이 구하는 식으로 할 수 있음.
        # Binary search도 가능.
        n = max(nums)
        sweep = [0] * (n+1)

        for num in nums:
            left = max(0, num - k)
            right = num + k + 1

            sweep[left] += 1
            if right <= n:
                sweep[right] -= 1

        ans = 1
        sw_accum = 0
        for sw in sweep:
            sw_accum += sw
            ans = max(ans, sw_accum)

        return ans
