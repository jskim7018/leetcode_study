from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_reverse = [0] * n
        curr_rev = 0
        ans = 0
        for i in range(n-k+1):
            curr_rev ^= prefix_reverse[i]
            actual = nums[i] ^ curr_rev
            if actual == 0:
                curr_rev ^= 1
                if i + k < n:
                    prefix_reverse[i+k] ^= 1
                ans += 1

        for i in range(n-k+1, n):
            curr_rev ^= prefix_reverse[i]
            actual = nums[i] ^ curr_rev
            if actual != 1:
                return -1

        return ans
