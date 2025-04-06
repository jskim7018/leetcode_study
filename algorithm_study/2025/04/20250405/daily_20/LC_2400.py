from functools import cache


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = int(1e9 + 7)

        @cache
        def solve(curr_pos, curr_k) -> int:
            if curr_k == 0 and curr_pos == endPos:
                return 1
            if curr_k == 0:
                return 0

            ret = (solve(curr_pos-1, curr_k-1)
                   + solve(curr_pos+1,curr_k-1))
            ret %= MOD

            return ret

        return solve(startPos, k)
