from typing import List
from operator import xor
from functools import reduce


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        # bit 별로. and 했을때 bit의 갯수가 각각 몇개인지 파악. 짝수면 버리고 홀수면 사용.
        arr1_xored = reduce(xor, arr1, 0)
        arr2_xored = reduce(xor, arr2, 0)

        return arr1_xored & arr2_xored
