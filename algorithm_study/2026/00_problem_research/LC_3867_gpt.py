from math import gcd


class Solution:
    def gcdSum(self, nums):
        n = len(nums)
        prefix = []

        mx = 0
        for v in nums:
            mx = max(mx, v)
            prefix.append(gcd(v, mx))

        prefix.sort()

        ans = 0

        for i in range(n // 2):
            a = prefix[i]
            b = prefix[n - 1 - i]

            if b % a == 0:
                ans += a
            else:
                ans += gcd(a, b)

        return ans