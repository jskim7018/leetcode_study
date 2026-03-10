from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나누기 없에 O(n)이 가능한가??
        # 숫자의 갯수가 총 60개정도니깐 그때그때 현재껏만 제외하고 곱해서 구한다?
        # 그럼 O(n*60) -> O(n)
        # prefix, suffix곱을 구한 다음 곱한다.
        # 보통 현재 제외 나머지면 prefix, suffix를 구해서 하는 것을 고려하자.
        # 그렇다면 O(1) space는 어떻게 가능?
        n = len(nums)
        ans = [1] * n

        prefix_prod = 1
        suffix_prod = 1

        for i in range(n):
            ans[i] *= prefix_prod
            ans[n-i-1] *= suffix_prod

            prefix_prod *= nums[i]
            suffix_prod *= nums[n-i-1]

        return ans
