from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        rem_to_num = defaultdict(list)

        for num in nums:
            rem = num % 3
            rem_to_num[rem].append(num)

        ans = 0
        for i in range(3):
            if i in rem_to_num:
                rem_to_num[i].sort(reverse=True)
                if len(rem_to_num[i]) >= 3:
                    ans = max(ans, sum(rem_to_num[i][:3]))

        if len(rem_to_num) >= 3:
            ans = max(ans, rem_to_num[0][0] + rem_to_num[1][0]
                      + rem_to_num[2][0])
        return ans
