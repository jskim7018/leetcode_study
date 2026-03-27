from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))

        @lru_cache(None)
        def dfs(pos, tight, has_diff):
            if pos == len(digits):
                return 1 if has_diff else 0

            limit = digits[pos] if tight else 9
            res = 0

            for d in range(limit + 1):
                if d in {3, 4, 7}:
                    continue

                new_tight = tight and (d == limit)
                new_has_diff = has_diff or (d in {2, 5, 6, 9})

                res += dfs(pos + 1, new_tight, new_has_diff)

            return res

        return dfs(0, True, False)