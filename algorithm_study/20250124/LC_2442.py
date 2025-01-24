from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        st = set(nums)

        for num in nums:
            num_str = str(num)
            num_str_rev = num_str[::-1]
            st.add(int(num_str_rev))

        return len(st)
