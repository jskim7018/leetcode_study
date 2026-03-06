class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues = sorted(set(rewardValues))
        max_sum = sum(rewardValues)
        # TODO: bit를 활용한 존재 여부.
        # Time complexity: O(n * max_reward / 64)
        # Which is extremely fast.
        dp = 1  # bitmask, bit i means sum i reachable

        for v in rewardValues:
            # Only extend sums < v
            mask = dp & ((1 << v) - 1)
            dp |= mask << v

        return dp.bit_length() - 1