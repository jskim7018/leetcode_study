from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        cnt = 0
        for i in range(0, n):
            if colors[i] != colors[i+1] != colors[i+2]:
                cnt += 1
        if colors[n-2] != colors[n-1] != colors[0]:
            cnt += 1
        if colors[n-1] != colors[0] != colors[1]:
            cnt += 1
        return cnt
