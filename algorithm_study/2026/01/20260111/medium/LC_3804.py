from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            st = set()
            _sum = 0
            for j in range(i, n):
                _sum += nums[j]
                st.add(nums[j])
                if _sum in st:
                    ans += 1
        return ans
