from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # 작게 시작해서 sliding window 방식으로 하는 투포인터.
        l = 0
        ans = n-1
        for r in range(n):
            while l < n and nums[l]*k < nums[r]:
                l += 1
            ans = min(ans, n - (r-l+1))

        return ans
