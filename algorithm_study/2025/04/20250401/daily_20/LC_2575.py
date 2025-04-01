from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        ans = []

        bef_digit = 0
        for c in word:
            digit = int(c) + bef_digit*10
            digit = digit % m

            if digit == 0:
                ans.append(1)
            else:
                ans.append(0)

            bef_digit = digit

        return ans
