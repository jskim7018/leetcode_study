from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 그냥 dp로도 가능
        # dp[i][j] -> 현재 i 까지했을때 j개의 k를 사용했을때 최대 길이.
        n = len(nums)
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        last_num_idx = dict()

        ans = 0
        for i in range(n):
            dp[i][0][1] = 1
            for j in range(k+1):
                prev_same_idx = float('-inf')
                # for prev same
                if nums[i] in last_num_idx:
                    prev_same_idx = last_num_idx[nums[i]]
                    dp[i][j][1] = max(dp[i][j][1], dp[prev_same_idx][j][1] + 1)

                # for prev not same
                if j - 1 >= 0:
                    # 지금께 들어 갔을때.
                    if prev_same_idx == i-1 and prev_same_idx >= 0:
                        dp[i][j][1] = max(dp[i][j][1], dp[prev_same_idx][j-1][0] + 1, dp[prev_same_idx][j-1][1] + 1)
                    elif prev_same_idx != i-1 and i-1 >= 0:
                        dp[i][j][1] = max(dp[i][j][1], dp[i-1][j - 1][0] + 1, dp[i-1][j - 1][1] + 1)
                    # 지금께 안들어 갔을때.
                    if prev_same_idx == i-1 and prev_same_idx >= 0:
                        dp[i][j][0] = max(dp[i][j][0], dp[prev_same_idx][j][1], dp[prev_same_idx][j][0])
                    elif prev_same_idx != i-1 and i-1 >= 0:
                        dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1], dp[i-1][j][0])
                ans = max(ans, dp[i][j][1], dp[i][j][0])
            last_num_idx[nums[i]] = i
        return ans
