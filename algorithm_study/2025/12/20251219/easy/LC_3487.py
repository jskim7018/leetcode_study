from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        st = set(nums)

        ans = 0

        positive_found = False

        max_neg = float('-inf')
        for element in st:
            if element > 0:
                ans += element
                positive_found = True
            else:
                max_neg = max(max_neg, element)

        if positive_found:
            return ans
        else:
            return max_neg
