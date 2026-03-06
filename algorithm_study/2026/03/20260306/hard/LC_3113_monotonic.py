from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        decr_stck = []

        ans = 0
        for num in nums:
            while decr_stck and decr_stck[-1][0] < num:
                decr_stck.pop()

            if decr_stck and decr_stck[-1][0] == num:
                decr_stck[-1][1] += 1
            else:
                decr_stck.append([num, 1])

            ans += decr_stck[-1][1]

        return ans
