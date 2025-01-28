from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        def powerset(idx: int, curr_nums:List[int], nums: List[int]):
            if idx >= n:
                curr_nums.sort()
                ans.add(tuple(curr_nums))
                return

            powerset(idx+1, curr_nums, nums)
            curr_nums.append(nums[idx])
            powerset(idx+1, curr_nums, nums)
            curr_nums.remove(nums[idx])

        powerset(0, [], nums)

        return list(ans)