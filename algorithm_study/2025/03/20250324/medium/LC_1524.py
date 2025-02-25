from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 0
        odd = 0

        ans = 0
        for a in arr:
            if a % 2 == 1:
                even, odd = odd, even
                odd += 1
            else:
                even += 1
            ans += odd
            ans %= 1e9+7
        return int(ans)
