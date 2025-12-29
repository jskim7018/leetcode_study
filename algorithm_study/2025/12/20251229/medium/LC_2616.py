from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        # binary search.
        # l = min of pairs, r = max of pairs.
        l = 0
        r = 0
        for i in range(1,n):
            r = max(r, nums[i]-nums[i-1])

        ans = 0
        while l<=r:
            m = (l+r)//2

            tmp_p = p
            i = 1
            while i < n and tmp_p:
                if nums[i]-nums[i-1] <= m:
                    i += 1
                    tmp_p -= 1
                i += 1
            if tmp_p == 0:
                r = m - 1
                ans = m
            else:
                l = m + 1

        return ans
