from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []

        pow = 0
        while n > 0:
            if n % 10 != 0:
                ans.append(n % 10 * (10**pow))
            n //= 10
            pow += 1
        ans.reverse()

        return ans
