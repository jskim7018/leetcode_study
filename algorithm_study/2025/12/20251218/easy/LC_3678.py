from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums)/len(nums)
        st = set(nums)

        if avg <= 0:
            need = 1
        else:
            need = int(avg) + 1

        while True:
            if need not in st:
                return need
            need += 1
        return -1
