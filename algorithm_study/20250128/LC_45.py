from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        l = r = 0

        ans = 0
        while r < n-1:
            farthest = 0
            for idx in range(l,r+1):
                farthest = max(farthest, idx + nums[idx])
            l = r+1
            r = farthest
            ans += 1

            if r >= n-1:
                return ans

        return ans
