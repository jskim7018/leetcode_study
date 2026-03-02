from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        j = n // 2
        count = 0

        # 어차피 최대 가능한게 n//2임. 그리고 반으로 나누면서 당연히 작은 것들과 큰것들을
        # 각각의 후보로 두는게 그리디 적으로 좋음.
        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return 2 * count