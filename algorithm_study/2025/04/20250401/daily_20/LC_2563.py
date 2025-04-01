from typing import List


# TODO check lower_bound logic and also check two pointer answer in editorial
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 0
        for i, num in enumerate(nums):

            lower_target = lower-num
            upper_target = upper-num

            l = i+1
            r = n-1

            while l<=r:
                mid = (l+r)//2
                if nums[mid] < lower_target:
                    l = mid+1
                elif nums[mid] >= lower_target:
                    r = mid-1
            lower_index = l

            l = i + 1
            r = n - 1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] <= upper_target:
                    l = mid+1
                elif nums[mid] > upper_target:
                    r = mid-1
            upper_index = r

            if lower_index <= upper_index:
                ans += (upper_index - lower_index + 1)

        return ans
