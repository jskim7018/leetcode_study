from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev_num_idx = {}

        def reverse_num(num: int) -> int:
            ret = 0
            while num > 0:
                ret *= 10
                ret += num%10
                num //= 10
            return ret

        ans = float('inf')
        for i, v in enumerate(nums):
            if v in rev_num_idx:
                ans = min(ans, i-rev_num_idx[v])
            rev_num_idx[reverse_num(v)] = i

        if ans == float('inf'):
            return -1
        else:
            return ans
