from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stck = deque()

        for c in s[::-1]:
            if c == 'a':
                if len(stck) < 2 or stck[-1] != 'b' or stck[-2] != 'c':
                    return False
                else:
                    stck.pop()
                    stck.pop()
            else:
                stck.append(c)
        if stck:
            return False
        else:
            return True
