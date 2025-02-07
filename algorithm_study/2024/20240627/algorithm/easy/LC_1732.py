from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        alt = 0
        for g in gain:
            alt += g
            ans = max(ans, alt)
        return ans
