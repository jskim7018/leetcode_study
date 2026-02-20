from functools import cache


class Solution:
    def canWin(self, currentState: str) -> bool:
        n = len(currentState)
        # TODO: 자세히 공부 필요.
        @cache
        def dp(idx: int) -> bool:
            if idx >= n - 1:
                return False

            ret = False
            if currentState[idx] == currentState[idx + 1] == '+':
                ret |= not dp(idx + 2)
                if idx + 2 < n and currentState[idx + 2] == '+':
                    ret |= not dp(idx + 3)
                    if idx + 3 < n and currentState[idx + 3] == '+':
                        ret |= dp(idx + 4)
                        if idx + 4 < n and currentState[idx + 4] == '+':
                            ret |= dp(idx + 5)
            else:
                ret |= dp(idx + 1)

            return ret

        return dp(0)