from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        _sum = sum(nums)

        rem = _sum % 3
        rem1 = []
        rem2 = []
        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)

        rem1.sort()
        rem2.sort()

        ans = 0
        if rem == 1:
            one_sub = 0
            if len(rem1) >= 1:
                one_sub = _sum - rem1[0]
            two_sub = 0
            if len(rem2) >= 2:
                two_sub = _sum - rem2[0] - rem2[1]
            return max(one_sub, two_sub)
        elif rem == 2:
            one_sub = 0
            if len(rem1) >= 2:
                one_sub = _sum - rem1[0] - rem1[1]
            two_sub = 0
            if len(rem2) >= 1:
                two_sub = _sum - rem2[0]
            return max(one_sub, two_sub)
        else:
            return _sum
