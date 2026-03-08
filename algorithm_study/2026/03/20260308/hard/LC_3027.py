from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        n = len(points)

        ans = 0
        for i in range(n):
            curr_max_y = float('-inf')

            for j in range(i+1, n):
                if points[i][1] >= points[j][1] > curr_max_y:
                    ans += 1
                    curr_max_y = max(curr_max_y, points[j][1])

        return ans