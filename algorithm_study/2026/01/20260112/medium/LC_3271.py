class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)

        ans = []
        for i in range(0, n, k):
            hashed = 0
            for j in range(k):
                hashed += ord(s[i+j]) - ord('a')

            hashed = chr(hashed % 26 + ord('a'))

            ans.append(hashed)

        return ''.join(ans)
