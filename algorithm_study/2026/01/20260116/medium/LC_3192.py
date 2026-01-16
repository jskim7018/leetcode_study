from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        flips = 0
        parity = 0
        for num in nums:
            if (num + parity) % 2 == 0:
                flips += 1

                parity += 1
                parity %= 2

        return flips
