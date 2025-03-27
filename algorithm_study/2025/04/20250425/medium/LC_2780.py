from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        counter = Counter(nums)

        most_common = counter.most_common(1)[0]
        most_occ = most_common[0]
        occ_cnt = most_common[1]

        curr_occ = 0
        for i in range(n):
            if nums[i] == most_occ:
                curr_occ += 1
            if curr_occ * 2 > i+1 and (occ_cnt-curr_occ) * 2 > n-i-1:
                return i

        return -1