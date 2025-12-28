from functools import cache


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(letter: str, curr_t: int) -> int:
            if curr_t <= 0:
                return 1

            diff_to_z = ord('z') - ord(letter)

            ret = 1
            if curr_t > diff_to_z:
                curr_t -= diff_to_z
                ret = dp('a', curr_t - 1) + dp('b', curr_t - 1)
                ret %= mod

            return ret

        ans = 0

        for ch in s:
            ans += dp(ch, t)
            ans %= mod

        return ans
