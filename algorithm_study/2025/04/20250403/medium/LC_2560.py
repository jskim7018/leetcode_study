from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_sorted = sorted(nums)
        l = 0
        r = n-1
        ans = 0
        while l<=r:
            mid = (l+r)//2
            i = 0
            cnt = 0
            isPossible = False
            while i<n:
                if nums[i] <= nums_sorted[mid]:
                   cnt += 1
                   i += 1
                if cnt >= k:
                    isPossible = True
                    break
                i += 1

            if isPossible:
                ans = nums_sorted[mid]
                r = mid - 1
            else:
                l = mid + 1

        return ans
