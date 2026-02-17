from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Goal: even 최대화, odd 최소화.
        # 고점 일때 넣고 저점 일때 뺀다를 반복.
        # TODO: DP 도 가능. new_odd = max(odd, even-x)

        is_even = True
        n = len(nums)
        ans = 0
        for i in range(n):
            if i == n-1:
                if is_even:
                    ans += nums[i]
            else:
                if is_even:
                    if nums[i+1] < nums[i]:
                        ans += nums[i]
                        is_even = False
                else:
                    if nums[i+1] > nums[i]:
                        ans -= nums[i]
                        is_even = True
        return ans
