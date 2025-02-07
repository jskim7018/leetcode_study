from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst = list()


        idx = 0
        while idx < len(nums):
            s = str("\"" + str(nums[idx]))

            is_idx_changed = False

            while idx < len(nums) and nums[idx+1]-1 == nums[idx]:
                idx += 1
                is_idx_changed = True
            if not is_idx_changed:
                idx += 1

            if idx != idx-1:
                s += "->" + str(nums[idx-1])
            s += "\""

            lst.append(s)

        return lst
