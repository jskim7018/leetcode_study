from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mp = defaultdict(list)

        for num in nums:
            maxim_digit = 0
            tmp_num = num
            while tmp_num > 0:
                maxim_digit = max(maxim_digit, tmp_num%10)
                tmp_num //= 10
            heapq.heappush(mp[maxim_digit], num)
            if len(mp[maxim_digit]) > 2:
                heapq.heappop(mp[maxim_digit])


        ans = -1
        for v in mp.values():
            if len(v) == 2:
               ans = max(ans, v[0] + v[1])

        return ans
