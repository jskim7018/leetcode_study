from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # prefix, suffix 정렬 count.
        # is there better way? less memory?
        # can do with just 2 variables saving count each time with sliding window
        n = len(nums)
        if n <= k*2:
            return []

        left_sorted_cnt = 1
        right_sorted_cnt = 1
        for i in range(1, k):
            if nums[i-1] >= nums[i]:
                left_sorted_cnt += 1
            else:
                left_sorted_cnt = 1

        for i in range(k + 2, 2*k+1):
            if nums[i - 1] <= nums[i]:
                right_sorted_cnt += 1
            else:
                right_sorted_cnt = 1

        ans = []
        if left_sorted_cnt == k and right_sorted_cnt == k:
            ans.append(k)

        for i in range(2*k+1, n):
            if nums[i-k-2] >= nums[i-k-1]:
                left_sorted_cnt += 1
            else:
                left_sorted_cnt = 1

            if nums[i - 1] <= nums[i]:
                right_sorted_cnt += 1
            else:
                right_sorted_cnt = 1

            if left_sorted_cnt >= k and right_sorted_cnt >= k:
                ans.append(i-k)

        return ans


