from collections import deque

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        d = deque(s)

        d.rotate(len(s)-k)

        return ''.join(d)
