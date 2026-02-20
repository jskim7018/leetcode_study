from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        sorted_num = [(num, i) for i, num in enumerate(nums)]
        sorted_num.sort()
        score = 0
        for num, idx in sorted_num:
            if idx not in marked:
                score += num
                marked.add(idx)
                marked.add(idx - 1)
                marked.add(idx + 1)

        return score
