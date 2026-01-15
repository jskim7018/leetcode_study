from typing import List
from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        nums_bin = [bin(num)[2:] for num in nums]

        ans = 0
        for p in permutations([0, 1, 2], 3):
            new_bin = nums_bin[p[0]] + nums_bin[p[1]] + nums_bin[p[2]]
            ans = max(ans, int(new_bin, 2))

        return ans
