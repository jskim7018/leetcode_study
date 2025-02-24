from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for i in range(n-2):
            for j in range(i+1, n-1):
                curr_sum = nums[i] + nums[j]

                to_find = target - curr_sum
                l = j+1
                r = n-1
                while l < r:
                    mid = (l+r)//2
                    if nums[mid] > to_find:
                        r = mid
                    else:
                        l = mid + 1
                if l < len(nums) and abs(curr_sum + nums[l] - target) < abs(ans - target):
                    ans = curr_sum + nums[l]

                if l-1 > j and abs(curr_sum + nums[l-1] - target) < abs(ans - target):
                    ans = curr_sum + nums[l-1]
        return ans
