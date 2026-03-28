from typing import List


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:

        minim_diff = float('inf')
        lst = []
        ans = []

        def backtrack(num: int, k_left: int):
            nonlocal minim_diff
            nonlocal ans

            if k_left == 1:
                lst.append(num)
                diff = lst[-1] - lst[0]
                if diff < minim_diff:
                    ans = list(lst)
                    minim_diff = diff
                lst.pop()
                return

            start = 1
            if len(lst):
                start = lst[-1]

            for div in range(start, int(num**0.5) + 1):
                if num % div == 0 and num // div >= div:
                    lst.append(div)
                    backtrack(num//div, k_left-1)
                    lst.pop()
        backtrack(n, k)

        return ans
