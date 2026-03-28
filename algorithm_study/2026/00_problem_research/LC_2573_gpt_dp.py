class Solution:
    def findTheString(self, lcp):
        n = len(lcp)

        # Step 1: Union-Find
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        # union if lcp[i][j] > 0
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        # Step 2: assign characters
        comp_to_char = {}
        cur = ord('a')
        word = [''] * n

        for i in range(n):
            p = find(i)
            if p not in comp_to_char:
                if cur > ord('z'):
                    return ""  # more than 26 groups
                comp_to_char[p] = chr(cur)
                cur += 1
            word[i] = comp_to_char[p]

        word = "".join(word)

        # Step 3: validate using DP
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word