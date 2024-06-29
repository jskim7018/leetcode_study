from typing import List
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        counter = Counter()
        ans = []
        for i in range(n):
            for j in range(n):
                counter[grid[i][j]] += 1


        ans.append(counter.most_common()[0][0]) # most common으로 찾을 수 있음
        for i in range(1, n*n+1):
            if i not in counter.keys():
                ans.append(i)
        return ans
