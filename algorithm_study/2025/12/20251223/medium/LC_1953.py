from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _max = max(milestones)
        total = sum(milestones)

        if _max > total - _max:
            return (total - _max)*2 + 1
        else:
            return total
