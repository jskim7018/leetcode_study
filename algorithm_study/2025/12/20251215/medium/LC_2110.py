from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def sum_formula(num: int) -> int:
            return ((num+1)*num) // 2

        prices.append(float('inf'))
        cnt = 1
        ans = 0

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                cnt += 1
            else:
                ans += sum_formula(cnt)
                cnt = 1

        return ans
