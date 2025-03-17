from typing import List
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        mp = dict()

        for i in range(len(nums)):
            num = nums[i]
            if num not in mp:
                mp[num] = []
            mp[num].append(i)

        ans = []
        for q in queries:
            num = nums[q]
            if len(mp[num]) <= 1:
                ans.append(-1)
            else:
                left = mp[num][bisect.bisect_left(mp[num], q)-1]
                right = mp[num][bisect.bisect_right(mp[num], q) % len(mp[num])]
                ans.append(min(min(abs(right-q),abs(right + len(nums)-q)),
                               min(abs(left-q),abs(q + len(nums)-left))))

        return ans
