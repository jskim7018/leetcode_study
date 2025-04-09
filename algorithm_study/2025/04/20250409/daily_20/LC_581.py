from typing import List
from collections import deque


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        stck = deque()

        left_idx = float('inf')
        for i in range(n):
            while stck and stck[-1][0] > nums[i]:
                popped = stck.pop()
                left_idx = min(left_idx, popped[1])
            stck.append((nums[i],i))

        right_idx = -1
        stck.clear()
        for i in range(n-1, -1,-1):
            while stck and stck[-1][0] < nums[i]:
                popped = stck.pop()
                right_idx = max(right_idx, popped[1])
            stck.append((nums[i],i))

        if right_idx == -1:
            return 0

        return right_idx-left_idx+1