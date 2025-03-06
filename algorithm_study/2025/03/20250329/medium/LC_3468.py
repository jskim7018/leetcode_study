from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        lower_bounds = []
        upper_bounds = []
        n = len(original)
        for i in range(n):
            lower_bounds.append(original[i] - bounds[i][0] + 1)
            upper_bounds.append(bounds[i][1] - original[i])
        print(lower_bounds)
        print(upper_bounds)

        return max(0, min(upper_bounds) + min(lower_bounds))
