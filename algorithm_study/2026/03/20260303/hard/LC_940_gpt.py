class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # Better memory usage than mine.
        MOD = 10 ** 9 + 7

        # dp = total subsequences including empty
        dp = 1

        # last[c] = dp value before last time we saw c
        last = {}

        for c in s:
            new_dp = (dp * 2) % MOD

            if c in last:
                new_dp = (new_dp - last[c] + MOD) % MOD

            last[c] = dp
            dp = new_dp

        # subtract empty subsequence
        return (dp - 1) % MOD