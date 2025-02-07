from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        s_idx = 0
        ans = 0
        for greed in g:
            while s_idx < len(s) and greed > s[s_idx]:
                s_idx += 1
            if s_idx >= len(s):
                break
            if greed <= s[s_idx]:
                ans += 1
                s_idx += 1
        return ans
