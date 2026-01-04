from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            divisor_lst = []
            for i in range(1, int(num**0.5)+1):
                if num % i == 0:
                    divisor_lst.append(i)
                    if i != num//i:
                        divisor_lst.append(num//i)
                if len(divisor_lst) > 4:
                    break
            if len(divisor_lst) == 4:
                for div in divisor_lst:
                    ans += div
        return ans
