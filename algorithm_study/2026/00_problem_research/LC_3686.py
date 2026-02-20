from collections import defaultdict
import copy


class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        mod = 10 ** 9 + 7
        # TODO: DP 말고, sliding window등의 방식이 안된다는 것을 어떻게 빠르게 파악할 수 있을까?
        dp = defaultdict(int)
        dp[(-1, -1)] = 1

        for num in nums:
            parity = num % 2
            new_dp = defaultdict(int)
            for (p1, p2), cnt in dp.items():
                if p1 == p2 == parity:
                    continue
                new_dp[(p2, parity)] += cnt
                new_dp[(p2, parity)] %= mod

            for k, cnt in new_dp.items():
                dp[k] += cnt
                dp[k] %= mod

        ans = 0
        for cnt in dp.values():
            ans += cnt
            ans %= mod

        return ans - 1
