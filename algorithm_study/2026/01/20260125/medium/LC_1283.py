from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()

        l = 1
        r = max(nums)

        ans = 0
        while l <= r:
            mid = (l+r)//2

            _sum = 0
            for num in nums:
                _sum += math.ceil(num/mid)

            if _sum <= threshold:
                ans = mid
                r = mid-1
            else:
                l = mid + 1

        return ans
