from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = dict()

        for idx, num in enumerate(nums):
            if num in mp.keys():
                if idx - mp[num] <= k:
                    return True
                else:
                    mp[num] = idx
            else:
                mp[num] = idx
        return False
