from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        prev_dp = [0] * 3
        prev_dp[0] = 1
        prev_dp[1] = 0
        prev_dp[2] = 1
        n = len(obstacles)
        for i in range(1, n):
            curr_obstacle = obstacles[i-1]-1
            curr_dp = [float('inf')] * 3
            for lane in range(3):
                if curr_obstacle != lane:
                    curr_dp[lane] = prev_dp[lane]
            if curr_obstacle != 0:
                curr_dp[0] = min(curr_dp[0], min(curr_dp[1], curr_dp[2]) + 1)
            if curr_obstacle != 1:
                curr_dp[1] = min(curr_dp[1], min(curr_dp[0], curr_dp[2]) + 1)
            if curr_obstacle != 2:
                curr_dp[2] = min(curr_dp[2], min(curr_dp[0], curr_dp[1]) + 1)
            prev_dp = curr_dp

        return min(prev_dp)
