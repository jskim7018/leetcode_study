class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        minim = s

        for i in range(1, n+1):
            minim = min(minim, s[:i][::-1]+s[i:], s[:n-i] + s[n-i:][::-1])

        return minim
