from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0

        bins = []
        for num in nums:
            bins.append(bin(num)[2:][::-1])

        ith = 0
        while ith <= 32:
            one_cnt = 0
            for bin_ in bins:
                if ith >= len(bin_):
                    continue
                if bin_[ith] == '1':
                    one_cnt += 1
            if one_cnt >= k:
                ans += (1 << ith)
            ith += 1

        return ans
