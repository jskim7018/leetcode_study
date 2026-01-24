from typing import List
from functools import reduce
from operator import xor


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)

        nums_xored = reduce(xor,nums)

        maxim = 0 # TODO: mask로 이름 지으면 좋을듯.
        for j in range(maximumBit):
            maxim += 1 << j
        ans = []

        for i in range(n-1, -1, -1):
            to_xor = ~nums_xored & maxim
            ans.append(to_xor)
            nums_xored ^= nums[i]

        return ans
