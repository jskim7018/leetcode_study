from typing import List
import math


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        # binary search 가능. Is there better way to do it?
        # k를 정하고 해본다. 그리고 k^2보다 작으면 된다.
        l = 1
        r = max(nums) + (int(len(nums) ** 0.5) + 1)

        ans = float('inf')
        while l <= r:
            mid = (l+r)//2
            ops = 0
            for num in nums:
                ops += math.ceil(num / mid)

            if ops <= mid**2:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
