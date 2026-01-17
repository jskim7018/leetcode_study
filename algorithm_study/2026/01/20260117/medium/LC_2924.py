from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        is_pointed = [0] * n

        for e in edges:
            is_pointed[e[1]] += 1

        ans = -1

        for i in range(n):
            if is_pointed[i] == 0:
                if ans != -1:
                    return -1
                else:
                    ans = i
        return ans
