from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        stck = deque()

        for c in s:
            if c != '*':
                stck.append(c)
            else:
                stck.pop()

        ans = ""
        for e in stck:
            ans += e
        return ans
