from typing import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        prefix = 0
        mp = defaultdict(int)
        mp[0] = 1
        for num in nums:
            if num % modulo == k:
                prefix += 1
                prefix %= modulo
            ans += mp[(prefix - k + modulo) % modulo]
            print(mp)
            print((prefix - k + modulo) % modulo)
            print(ans)
            mp[prefix] += 1
        return ans
