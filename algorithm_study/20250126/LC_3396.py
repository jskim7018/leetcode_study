from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        st = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in st:
                left_over = n - len(st)
                op_cnt = math.ceil(left_over / 3)
                return op_cnt
            else:
                st.add(nums[i])

        return 0
