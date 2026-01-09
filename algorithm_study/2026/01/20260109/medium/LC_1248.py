from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt_odds = 0
        prefix_freq = defaultdict(int)

        prefix_freq[0] = 1

        ans = 0
        for num in nums:
            if num % 2 == 1:
                cnt_odds += 1

            prefix_freq[cnt_odds] += 1
            if cnt_odds - k in prefix_freq:
                ans += prefix_freq[cnt_odds - k]
        return ans
