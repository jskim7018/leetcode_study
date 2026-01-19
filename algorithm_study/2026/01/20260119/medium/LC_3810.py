from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in range(n):
            if nums[i] != target[i]:
                st.add(nums[i])

        return len(st)
