class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5

        # TODO: return math.comb(n + 4, 4) 원리, stars and bars problem.
        for i in range(2, n+1):
            new_dp = [0] * 5

            for i in range(5):
                for j in range(i+1):
                    new_dp[i] += dp[j]

            dp = new_dp
        return sum(dp)
