from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        streak = 1
        special_streak = [1] * n

        for i in range(1, n):
            if nums[i-1] % 2 != nums[i] % 2:
                streak += 1
            else:
                streak = 1

            special_streak[i] = streak

        ans = []
        for q in queries:
            _from, _to = q
            if special_streak[_to] >= _to - _from + 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans
