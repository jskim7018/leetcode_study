class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stck = list()
        n = len(s)
        m = len(part)

        for i in range(n):
            stck.append(s[i])

            if len(stck) >= m and ''.join(stck[len(stck)-m:]) == part:
                for j in range(m):
                    stck.pop()

        return ''.join(stck)
