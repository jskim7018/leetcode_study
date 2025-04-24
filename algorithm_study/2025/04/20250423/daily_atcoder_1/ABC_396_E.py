import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys

sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append((y, z))
    g[y].append((x, z))
visited = [False] * n
val = [-1] * n


q = []


def dfs(v):
    visited[v] = True
    for u, w in g[v]:
        if not visited[u]:
            val[u] = val[v] ^ w
            q.append(u)
            dfs(u)
        else:
            if val[u] != val[v] ^ w:
                print("-1")
                exit()


ans = [0] * n
for st in range(n):
    if visited[st]:
        continue
    val[st] = 0 # baseline as 0
    q = [st]
    dfs(st)
    for i in range(30):
        cnt = 0
        for j in q:
            if val[j] & (1 << i):
                cnt += 1
        if cnt < len(q) - cnt:
            for j in q:
                if val[j] & (1 << i):
                    ans[j] |= 1 << i
        else:
            for j in q:
                if not val[j] & (1 << i):
                    ans[j] |= 1 << i
print(*ans)
