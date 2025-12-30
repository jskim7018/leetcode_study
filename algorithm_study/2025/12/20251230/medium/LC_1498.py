from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7

        n = len(nums)
        nums.sort()

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % mod

        ans = 0
        for i in range(n):
            if nums[i]*2 <= target:
                ans += 1
            if nums[i] > target:
                break
            l = 0
            r = i-1
            possible = target - nums[i]
            best_idx = -1
            while l <= r:
                m = (l+r)//2
                if nums[m] <= possible:
                    best_idx = m
                    l = m+1
                else:
                    r = m-1
            ans += (pow2[best_idx+1]-1) * pow2[max(0, (i-best_idx-1))]
            ans %= mod

        return ans
