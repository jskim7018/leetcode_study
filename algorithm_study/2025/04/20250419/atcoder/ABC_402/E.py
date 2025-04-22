from functools import cache
import sys
sys.setrecursionlimit(10**5)

N, X = map(int, input().split())

problems = []

for i in range(N):
    S, C, P = map(int,input().split())
    problems.append((S,C,P/100))

@cache
def solve(coins, solved_mask) -> float:
    if coins == 0:
        return 0.0
    ret = 0.0
    for i in range(N):
        S, C, P = problems[i]
        if not (solved_mask >> i) & 1 and coins >= C:
            new_mask = solved_mask | (1 << i)

            solved = P * (S + solve(coins - C, new_mask))
            failed = (1 - P) * solve(coins - C, solved_mask)

            ret = max(ret, solved + failed)
    return ret

print(solve(X, 0))
solve.cache_clear()