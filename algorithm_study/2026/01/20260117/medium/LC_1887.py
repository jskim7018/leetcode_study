from typing import List
from collections import defaultdict


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        num_to_freq = list(counter.items())

        num_to_freq.sort(reverse = True)

        n = len(num_to_freq)

        ans = 0
        for i in range(n):
            _, freq = num_to_freq[i]
            ans += freq*(n-i-1)

        return ans
