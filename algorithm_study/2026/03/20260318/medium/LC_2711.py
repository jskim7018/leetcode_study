from typing import List
from collections import defaultdict


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        # 일단 2 pass는 필수적.
        # 일단 각 시작점 부터 오른쪽 끝까지의 counter를 만들어 놓는다.
        # 그리고 순회하면서 counter를 조정하여 구한다.
        m, n = len(grid), len(grid[0])

        counter_from_start = defaultdict(lambda: defaultdict(int))

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            y = i
            x = 0
            counter = counter_from_start[(y, x)]
            while y < m and x < n:
                ans[y][x] = len(counter)
                counter[grid[y][x]] += 1
                y += 1
                x += 1

        for j in range(1, n):
            y = 0
            x = j
            counter = counter_from_start[(y, x)]
            while y < m and x < n:
                ans[y][x] = len(counter)
                counter[grid[y][x]] += 1
                y += 1
                x += 1

        for i in range(m):
            y = i
            x = 0
            counter = counter_from_start[(y, x)]
            while y < m and x < n:
                counter[grid[y][x]] -= 1
                if counter[grid[y][x]] == 0:
                    del counter[grid[y][x]]
                ans[y][x] = abs(ans[y][x] - len(counter))
                y += 1
                x += 1

        for j in range(1, n):
            y = 0
            x = j
            counter = counter_from_start[(y, x)]
            while y < m and x < n:
                counter[grid[y][x]] -= 1
                if counter[grid[y][x]] == 0:
                    del counter[grid[y][x]]
                ans[y][x] = abs(ans[y][x] - len(counter))
                y += 1
                x += 1

        return ans
