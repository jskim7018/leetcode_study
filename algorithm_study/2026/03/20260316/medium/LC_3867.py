from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        n = len(nums)
        maxim = float('-inf')

        for num in nums:
            maxim = max(maxim, num)
            prefix_gcd.append(gcd(num, maxim))

        prefix_gcd.sort()
        ans = 0
        for i in range(n//2):
            ans += gcd(prefix_gcd[i], prefix_gcd[n-i-1])

        return ans
