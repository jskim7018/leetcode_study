from typing import List
from collections import defaultdict
from functools import cache


class RollingHash:
    def __init__(self, s: str):
        self.mod = 10**9 + 7
        self.base = 91138233   # any large random odd number
        self.n = len(s)
        self.cache = dict()

        self.h = [0] * (self.n + 1)
        self.p = [1] * (self.n + 1)

        for i in range(self.n):
            self.h[i + 1] = (self.h[i] * self.base + ord(s[i])) % self.mod
            self.p[i + 1] = (self.p[i] * self.base) % self.mod

    def get(self, l: int, r: int) -> int:
        if (l, r) in self.cache:
            return self.cache[(l,r)]
        else:
            self.cache[(l,r)] = (self.h[r] - self.h[l] * self.p[r - l]) % self.mod
        # returns hash of s[l:r]
            return self.cache[(l,r)]

    def getAll(self) -> int:
        return self.get(0, self.n)

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 각 original -> changed까지 최적을 cost 구해야함. floyd-warshall
        # 그다음 dp 하면 끝 <- easy part.
        # rolling hash 필요?
        # TODO: 자세히 공부 필요. chatgpt가 만든 솔루션과 내것의 차이 정확히 이해하고
        # TODO: 어떻게 더 효율적으로 짠건지 분석 제대로 하자.
        # TODO: 이 문제는 정말 자세히 분석하자!!

        n = len(original)
        dp = defaultdict(lambda: defaultdict(lambda: float('inf')))
        rh_original = [0] * n
        rh_changed = [0] * n

        for i in range(n):
            rh_o = RollingHash(original[i])
            rh_c = RollingHash(changed[i])
            rh_original[i] = rh_o.getAll()
            rh_changed[i] = rh_c.getAll()
            dp[rh_original[i]][rh_changed[i]] = min(dp[rh_original[i]][rh_changed[i]], cost[i])

        # floyd-warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[rh_original[i]][rh_changed[k]] + dp[rh_changed[k]][rh_changed[j]] < dp[rh_original[i]][rh_changed[j]]:
                        dp[rh_original[i]][rh_changed[j]] = dp[rh_original[i]][rh_changed[k]] + dp[rh_changed[k]][rh_changed[j]]

        rh_source = RollingHash(source)
        rh_target = RollingHash(target)

        solve = [float('inf')] * (len(source)+1)
        solve[0] = 0
        for i in range(1, len(source)+1):
            for j in range(max(0, i-105), i+1):
                if rh_source.get(j, i) != rh_target.get(j, i):
                    solve[i] = min(solve[i], solve[j] + dp[rh_source.get(j, i)][rh_target.get(j, i)])
                else:
                    solve[i] = min(solve[i], solve[j])

        solved = solve[len(source)]
        if solved == float('inf'):
            return -1
        else:
            return int(solved)

        # @cache
        # def solve(idx: int) -> int:
        #     if idx >= len(source):
        #         return 0
        #
        #     ret = float('inf')
        #     for i in range(idx, len(source)):
        #         if rh_source.get(idx, i+1) == rh_target.get(idx, i+1):
        #             ret = min(ret, solve(i + 1))
        #         elif dp[rh_source.get(idx, i+1)][rh_target.get(idx, i+1)] != float('inf'):
        #             ret = min(ret, dp[rh_source.get(idx, i+1)][rh_target.get(idx, i+1)] + solve(i+1))
        #     return ret
        #
        # solved = solve(0)
        # if solved == float('inf'):
        #     return -1
        # else:
        #     return solved
