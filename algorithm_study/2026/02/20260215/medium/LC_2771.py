from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] -> longest up to i when chosen j (nums1 or nums2 for current)
        # can optimize by only keeping prev (prev_dp[j] and curr_dp[j])
        n = len(nums1)
        prev_dp = [1, 1]
        ans = 1
        for i in range(1, n):
            curr_dp = [1, 1]
            if nums1[i-1] <= nums1[i]:
                curr_dp[0] = prev_dp[0] + 1
            if nums2[i-1] <= nums1[i]:
                curr_dp[0] = max(curr_dp[0], prev_dp[1] + 1)

            if nums1[i-1] <= nums2[i]:
                curr_dp[1] = prev_dp[0] + 1
            if nums2[i-1] <= nums2[i]:
                curr_dp[1] = max(curr_dp[1], prev_dp[1] + 1)

            ans = max(ans, curr_dp[0], curr_dp[1])
            prev_dp = curr_dp

        return ans
