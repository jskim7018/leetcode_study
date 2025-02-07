from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()

        ans = []
        for i in range(len(nums)):
            curr_num = nums[i]
            l = i+1
            r = len(nums)-1
            m = (l+r)//2

            to_find = target-curr_num[0]
            while l<=r:
                if nums[m][0] == to_find:
                    ans.append(curr_num[1])
                    ans.append(nums[m][1])
                    break
                elif nums[m][0] < to_find:
                    l = m+1
                else:
                    r = m-1
                m = (l+r)//2

            if len(ans) != 0:
                return ans

        return []
