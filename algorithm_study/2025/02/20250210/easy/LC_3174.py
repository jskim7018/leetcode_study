from collections import deque

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c.isdigit() and len(stack) > 0:
                stack.pop()
            else:
                stack.append(c)

        ans = ""
        for c in stack:
            ans += c

        return ans
