from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)

        st = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            num = digits[i] * 100

            for j in range(n):
                if i == j:
                    continue
                num += digits[j] * 10
                for k in range(n):
                    if k==i or k==j:
                        continue
                    num += digits[k]
                    if num % 2 == 0:
                        st.add(num)
                    num -= digits[k]
                num -= digits[j] * 10

        return len(st)
