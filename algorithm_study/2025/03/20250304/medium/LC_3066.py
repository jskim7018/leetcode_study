from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        ans = 0
        while nums[0] < k:
            ans += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x,y)*2 + max(x,y))

        return ans
