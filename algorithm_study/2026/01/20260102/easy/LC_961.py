from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        st = set()

        for num in nums:
            if num in st:
                return num
            else:
                st.add(num)
        return -1
    