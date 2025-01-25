from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                for a in range(num):
                    if (a | (a+1)) == num:
                        ans.append(a)
                        break

        return ans
