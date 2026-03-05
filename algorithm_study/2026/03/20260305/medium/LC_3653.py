from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # 그냥 한다? O(10^6)
        mod = 10**9 + 7
        for q in queries:
            l, r, k, v = q

            for i in range(l, r+1, k):
                nums[i] *= v
                nums[i] %= mod

        ans = 0
        for num in nums:
            ans ^= num

        return ans
