from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        n = len(points)

        ans = 0
        for i in range(n):
            curr_y = points[i][1]
            curr_least_y = float('-inf')
            for j in range(i+1, n):
                try_y = points[j][1]
                if curr_least_y < try_y <= curr_y:
                    ans += 1
                    curr_least_y = try_y

        return ans
