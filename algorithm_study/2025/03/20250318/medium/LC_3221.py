from typing import List
import heapq

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        ans = 0
        mx = 0
        for num in reversed(nums[1:]):
            mx = max(mx, num)
            ans += mx

        return ans
