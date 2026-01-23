from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)

        ans = [[0 for i in range(n)] for _ in range(2)]

        for j in range(n):
            if colsum[j] == 2:
                if upper > 0 and lower > 0:
                    upper -= 1
                    lower -= 1
                    ans[0][j] = 1
                    ans[1][j] = 1
                else:
                    return []
            elif colsum[j] == 1:
                if upper > 0 and upper >= lower:
                    ans[0][j] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][j] = 1
                    lower -= 1
                else:
                    return []
        if upper == 0 and lower == 0:
            return ans
        else:
            return []
