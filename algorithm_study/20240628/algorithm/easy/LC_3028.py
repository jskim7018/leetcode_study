from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr_pos = 0
        ans = 0
        for num in nums:
            curr_pos += num
            if curr_pos == 0:
                ans += 1
        return ans
