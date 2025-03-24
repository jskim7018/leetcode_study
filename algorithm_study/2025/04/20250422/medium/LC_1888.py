from functools import cache


# TODO: O(N) sliding window 방법 이해하기
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        isEven = n%2 == 0

        @cache
        def solve(idx, isOneNeed:bool, isSkipUsed:bool):
            if idx >= n:
                return 0

            if isOneNeed:
                ret = solve(idx+1, not isOneNeed, isSkipUsed) + (s[idx] == '0')
            else:
                ret = solve(idx+1, not isOneNeed, isSkipUsed) + (s[idx] == '1')

            if not isEven and not isSkipUsed:
                ret = min(ret, solve(idx+1, isOneNeed, True))

            return ret

        return min(solve(0, True, False),
                   solve(0, False, False))
