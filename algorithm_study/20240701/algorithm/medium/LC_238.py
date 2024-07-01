from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l = [1]
        prod_r = [1]
        for i in range(0, len(nums)):
            prod_l.append(prod_l[i] * nums[i])
            prod_r.append(prod_r[i] * nums[-i-1])
        ans = []
        for i in range(1, len(prod_l)):
            ans.append(prod_l[i-1] * prod_r[-i-1])
        return ans
