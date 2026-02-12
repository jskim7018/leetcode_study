from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        # 모두 AND 해서 minimum sum 구함.
        # 모두 AND 한게 0이 아니면 정답은 1, 0이면 greedy로 and 0 되는 갯수 찾기.
        n = len(nums)
        all_and = nums[0]
        for i in range(1, n):
            all_and &= nums[i]

        if all_and != 0:
            return 1
        else:
            cnt = 0
            curr_and = nums[0]
            for i in range(1, n):
                if curr_and == 0:
                    cnt += 1
                    curr_and = nums[i]
                else:
                    curr_and &= nums[i]
            if curr_and == 0:
                cnt += 1
            return cnt
