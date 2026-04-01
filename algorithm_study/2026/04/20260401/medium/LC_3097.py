from typing import List
from collections import defaultdict


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window should work
        n = len(nums)

        l = 0
        bit_cnt = defaultdict(int)
        ans = float('inf')
        curr_sum = 0
        for r in range(n):
            num = nums[r]
            pos = 0
            while num > 0:
                bit = num % 2
                if bit == 1:
                    if bit_cnt[pos] == 0:
                        curr_sum += pow(2, pos)
                    bit_cnt[pos] += 1
                pos += 1
                num //= 2

            while l <= r and  curr_sum >= k:
                ans = min(ans, r-l+1)
                num = nums[l]
                pos = 0
                while num > 0:
                    bit = num % 2
                    if bit == 1:
                        bit_cnt[pos] -= 1
                        if bit_cnt[pos] == 0:
                            del bit_cnt[pos]
                            curr_sum -= pow(2, pos)
                    pos += 1
                    num //= 2
                l += 1

        if ans == float('inf'):
            return -1
        else:
            return ans
