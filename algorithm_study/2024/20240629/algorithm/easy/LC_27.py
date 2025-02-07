from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        r = len(nums)-1
        while l <= r:
            while l < len(nums) and nums[l] != val and l <= r:
                l += 1
            while r >= 0 and nums[r] == val and l <= r:
                r -= 1
            if l >= r:
                break
            nums[l], nums[r] = nums[r], nums[l]
        return l

"""
# Python3
아래는 더 간결한 방법. 양끝에서 투 포인터가 아닌 시작에서 투포인터로 하는 방법.
교체만 하면 되기에 뒤에서 양끝에서 굳이 시작해서 복잡도를 늘릴필요가 없었음.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
"""