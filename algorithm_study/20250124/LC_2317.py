from typing import List
from functools import reduce


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:

        result = reduce(lambda x,y: x|y, nums)
        return result
