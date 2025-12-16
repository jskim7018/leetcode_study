from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        techniques = [(a-b, a,b) for a,b in zip(technique1, technique2)]

        techniques.sort(key=lambda x: x[0], reverse=True)

        ans = 0
        for t in techniques:
            if k > 0:
                ans += t[1]
                k -= 1
            else:
                ans += max(t[1], t[2])

        return ans
