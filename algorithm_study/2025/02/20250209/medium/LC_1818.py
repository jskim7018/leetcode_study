from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        MOD = int(1E9+7)
        print(MOD)
        total_sum = 0
        idx_diff = {}

        for i in range(n):
            diff = abs(nums1[i]-nums2[i])
            idx_diff[i] = diff
            total_sum += diff

        nums1_sorted = sorted(nums1)

        ans = total_sum
        for i in range(n):
            new_sum = total_sum - idx_diff[i]

            curr = nums2[i]
            idx = bisect.bisect_left(nums1_sorted, curr)

            new_sum1 = new_sum + abs(nums1_sorted[idx-1]-nums2[i])

            new_sum2 = total_sum
            if idx < n:
                new_sum2 = new_sum + abs(nums1_sorted[idx] - nums2[i])
            ans = min(ans, new_sum1, new_sum2)
        ans %= MOD

        return ans
