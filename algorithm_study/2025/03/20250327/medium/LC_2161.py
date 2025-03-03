from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        largers = []

        same_cnt = 0
        ans = []
        for num in nums:
            if num > pivot:
                largers.append(num)
            elif num < pivot:
                ans.append(num)
            else:
                same_cnt+=1
        for _ in range(same_cnt):
            ans.append(pivot)
        ans = ans + largers

        return ans
