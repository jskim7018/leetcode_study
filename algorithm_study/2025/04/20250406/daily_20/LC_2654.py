from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ones = nums.count(1)
        if ones > 0:
            return n-ones
        else:
            ans = float('inf')
            for j in range(1, n):
                cnt = 0
                tmp_nums = list(nums)
                for i in range(j, n):
                    gcd_ = gcd(tmp_nums[i-1], tmp_nums[i])
                    tmp_nums[i] = gcd_
                    if gcd_ == 1:
                        ans = min(ans, n+cnt)
                        break
                    else:
                        cnt += 1
                        tmp_nums[i] = gcd_
            if ans == float('inf'):
                return -1
            else:
                return ans
