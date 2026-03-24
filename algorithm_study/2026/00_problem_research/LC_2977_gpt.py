from collections import defaultdict
import math

MOD = 10**9 + 7
INF = 10**18

# -------- Rolling Hash (double) ----------
class RollingHash:
    def __init__(self, s):
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9
        self.base = 91138233
        n = len(s)

        self.p1 = [1] * (n + 1)
        self.p2 = [1] * (n + 1)
        for i in range(n):
            self.p1[i+1] = self.p1[i] * self.base % self.mod1
            self.p2[i+1] = self.p2[i] * self.base % self.mod2

        self.h1 = [0] * (n + 1)
        self.h2 = [0] * (n + 1)
        for i, c in enumerate(s):
            v = ord(c) - 96
            self.h1[i+1] = (self.h1[i] * self.base + v) % self.mod1
            self.h2[i+1] = (self.h2[i] * self.base + v) % self.mod2

    def get(self, l, r):
        x1 = (self.h1[r] - self.h1[l] * self.p1[r-l]) % self.mod1
        x2 = (self.h2[r] - self.h2[l] * self.p2[r-l]) % self.mod2
        return (x1, x2)

# -------- Main Solution ----------
def minimumCost(source, target, original, changed, cost):
    n = len(source)

    rules = defaultdict(list)
    for o, c, w in zip(original, changed, cost):
        rules[len(o)].append((o, c, w))

    # Precompute shortest paths per length
    trans_cost = dict()

    for L, arr in rules.items():
        nodes = set()
        for o, c, _ in arr:
            nodes.add(o)
            nodes.add(c)
        nodes = list(nodes)
        idx = {s: i for i, s in enumerate(nodes)}
        m = len(nodes)

        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in arr:
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        # Floyd–Warshall
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        trans_cost[L] = (idx, dist)

    dp = [INF] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        # no operation
        if source[i] == target[i]:
            dp[i] = dp[i + 1]

        for L, (idx, dist) in trans_cost.items():
            if i + L > n:
                continue

            s = source[i:i+L]
            t = target[i:i+L]

            if s in idx and t in idx:
                c = dist[idx[s]][idx[t]]
                if c < INF:
                    dp[i] = min(dp[i], c + dp[i + L])

    return -1 if dp[0] == INF else dp[0]
