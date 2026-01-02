from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        l_curr = nums[0] - k
        stopped_idx = n
        ans = 0
        for i in range(n):
            if nums[i] >= l_curr:
                l_curr = max(nums[i] - k, l_curr)
                l_curr += 1
                ans += 1
            else:
                stopped_idx = i
                break
        r_curr = nums[-1] + k
        for i in range(n-1, stopped_idx-1, -1):
            if r_curr < l_curr:
                break
            if r_curr >= nums[i]:
                r_curr = min(nums[i] + k, r_curr)
                if r_curr < l_curr:
                    break
                r_curr -= 1
                ans += 1
            elif nums[i]-k <= r_curr <= nums[i]:
                r_curr = r_curr
                if r_curr < l_curr:
                    break
                r_curr -= 1
                ans += 1
        return ans
