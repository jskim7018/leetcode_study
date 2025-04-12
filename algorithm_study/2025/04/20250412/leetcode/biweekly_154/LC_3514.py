from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        st = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                st.add(nums[i]^nums[j])
        st2 = set()
        for i in range(len(nums)):
            for e in st:
                st2.add(e^nums[i])

        return len(st2)
