from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        visited = [False] * len(nums)
        picked_arr = []
        ans = []

        def permutations(picked_cnt: int):
            if picked_cnt == len(nums):
                ans.append(tuple(picked_arr))

            st = set()
            for i in range(len(nums)):
                if not visited[i] and nums[i] not in st:
                    visited[i] = True
                    picked_arr.append(nums[i])
                    st.add(nums[i])
                    permutations(picked_cnt + 1)
                    visited[i] = False
                    picked_arr.pop()

        permutations(0)

        return ans
