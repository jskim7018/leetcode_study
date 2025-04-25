from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a:int, b:int) -> int:
            return (a*b)//gcd(a,b)


        ans = 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                lcm_ = lcm(curr, nums[j])
                if lcm_ == k:
                    ans += 1
                elif lcm_ > k:
                    break
                curr = lcm_
        return ans
