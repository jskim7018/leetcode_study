from typing import List
from math import prod


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        ans = 1
        pos_prod = 1
        neg = []
        pos_exist = False
        zero_exist = False
        for num in nums:
            if num > 0:
                pos_prod *= num
                pos_exist = True
            elif num < 0:
                neg.append(num)
            else:
                zero_exist = True
        ans *= pos_prod
        neg.sort()
        if len(neg) >= 2:
            if len(neg) % 2 == 1:
                neg = neg[:-1]
            ans *= prod(neg)
        elif not pos_exist:
            if zero_exist:
                ans = 0
            elif len(neg) == 1:
                ans = neg[0]

        return ans
