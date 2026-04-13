class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)

        nums = [ord(c) - ord('A') for c in word]

        dp = [0] * 26  # key fix

        for i in range(1, len(nums)):
            new_dp = [float('inf')] * 26
            curr = nums[i]
            prev = nums[i - 1]

            for j in range(26):
                # 1. same finger
                new_dp[j] = min(new_dp[j], dp[j] + dist(prev, curr))

                # 2. other finger
                new_dp[prev] = min(new_dp[prev], dp[j] + dist(j, curr))

            dp = new_dp

        return min(dp)