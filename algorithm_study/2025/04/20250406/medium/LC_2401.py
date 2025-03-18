from typing import List
from collections import defaultdict

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        bit_cnt = defaultdict(int)
        cnt_more_than_one = 0
        def set_bit_cnt(num, isIncrease: bool):
            nonlocal cnt_more_than_one
            for i in range(30):
                if (num >> i) & 1 == 1:
                    if isIncrease:
                        bit_cnt[i] += 1
                        if bit_cnt[i] > 1:
                            cnt_more_than_one += 1
                    else:
                        bit_cnt[i] -= 1
                        if bit_cnt[i] == 1:
                            cnt_more_than_one -= 1

        l = 0
        ans = 0
        for r in range(n):
            set_bit_cnt(nums[r], True)

            while cnt_more_than_one and l < n:
                set_bit_cnt(nums[l], False)
                l += 1
            ans = max(ans,r-l+1)

        return ans
