from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        max_subseq_to = defaultdict(int) # dp라고 볼 수 있음.

        ans = 1
        for num in arr:
            prev = num - difference

            max_subseq_to[num] = max(max_subseq_to[num],
                                     max_subseq_to[prev] + 1)
            ans = max(ans, max_subseq_to[num])

        return ans
