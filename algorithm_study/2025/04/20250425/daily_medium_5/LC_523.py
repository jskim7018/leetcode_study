from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = 0
        mp = dict()
        mp[0] = -1
        for i in range(n):
            prefix += nums[i]
            modulus = prefix % k
            if modulus in mp and i-mp[modulus] >= 2:
                return True
            elif modulus not in mp:
                mp[modulus] = i

        return False
