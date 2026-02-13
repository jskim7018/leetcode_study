from typing import List
from collections import defaultdict, deque


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        col_deque = defaultdict(deque)

        m = len(nums)
        max_idx = -1
        for i in range(m):
            for j in range(len(nums[i])):
                col_deque[j+i].appendleft(nums[i][j])
                max_idx = max(max_idx, j+i)

        # max idx만 구하면 sorted도 필요 없음.
        ans = []
        for idx in range(max_idx + 1):
            ans.extend(col_deque[idx])

        return ans
