from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = float("inf")

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] > nums[k]:
                        ans = min(ans, nums[i] + nums[j] + nums[k])

        if ans == float("inf"):
            return -1

        return ans

"""
O(n)으로 하는 방법
양쪽의 min 배열을 만든 후 O(n)으로 min을 각각 구해서 각 위치에 대한 최적의 산을 바로 구한다.
ref: https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/solutions/4195273/c-java-python-javascript-explained/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0] * n
        r = [0] * n

        l[0] = nums[0]
        r[n - 1] = nums[n - 1]

        for i in range(1, n):
            l[i] = min(l[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            r[i] = min(r[i + 1], nums[i])

        mn = 2_000_000_000

        for i in range(1, n - 1):
            if l[i] < nums[i] and r[i] < nums[i]:
                mn = min(mn, l[i] + nums[i] + r[i])

        return -1 if mn == 2_000_000_000 else mn
"""