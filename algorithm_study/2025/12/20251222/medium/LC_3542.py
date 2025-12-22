from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        stack = list()

        ans = 0
        for num in nums:
            if not stack or stack[-1] <= num:
                stack.append(num)
            else:
                prev = -1
                while stack and stack[-1] > num:
                    if stack[-1] != prev and stack[-1] != 0:
                        ans += 1
                    prev = stack.pop()
                stack.append(num)
        prev = -1
        while stack:
            if stack[-1] != prev and stack[-1] != 0:
                ans += 1
            prev = stack.pop()
        return ans
