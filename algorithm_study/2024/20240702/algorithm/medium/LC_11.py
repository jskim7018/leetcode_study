from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        max_ = 0
        while l != r:
            max_ = max(max_, min(height[l], height[r]) * (r-l))
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max_
