from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [num for num in nums if num != 0]
        nums.sort()

        n = len(nums)

        ans = 0
        for i in range(n-1, -1, -1):
            largest = nums[i]
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > largest:
                    ans += ((r-l+1)*(r-l)) // 2
                    r -= 1
                else:
                    l += 1

        return ans
