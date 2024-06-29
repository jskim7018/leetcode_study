from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for num in nums:
            if bin(num)[-1] == '0':
                cnt += 1
                if cnt > 1:
                    return True
        return False
