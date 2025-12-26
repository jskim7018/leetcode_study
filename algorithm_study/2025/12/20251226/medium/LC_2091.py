from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        _min = float('inf')

        _min_idx = -1
        _max_idx = -1
        _max = float('-inf')

        for i, num in enumerate(nums):
            if num < _min:
                _min = num
                _min_idx = i
            if num > _max:
                _max = num
                _max_idx = i

        min_left_dist = _min_idx + 1
        max_left_dist = _max_idx + 1
        min_right_dist = len(nums) - _min_idx
        max_right_dist = len(nums) - _max_idx

        ans = min(max(min_left_dist, max_left_dist),
                  max(min_right_dist, max_right_dist),
                  min_right_dist + max_left_dist,
                  min_left_dist + max_right_dist)

        return ans
