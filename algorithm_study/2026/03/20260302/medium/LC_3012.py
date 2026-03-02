from typing import List
import math


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        # 0을 최대한 적게 만드는게 목표.
        # 큰 것 작은 것 이렇게 2개 있으면 작은 것을 남기면 큰 것을 하나씩 제거하나 효과.
        # -> 모두 다르면 1개만 남기고 끝낼 수 있음.
        # 중복이 있을 경우? -> 중복 2개당 0 한개
        # 5 5 5 5 6 7 8 9

        # 작은 것 하나가 다 없엘 수 있음.
        # 가장 작은게 중복이 없으면 그냥 1
        # 가장 작은게 중복이 있다면?

        # gcd 찾음. gcd의 갯수 (math.ceil(gcd_count/2))로 끝.
        # TODO: gcd를 안구해도 됨. 가장 작은 값이 모두 나누면 gcd는 해당 값이고 아니면 밑에 값이 됨. 그리고 밑에 값은 무조건 1.
        n = len(nums)
        _gcd = nums[0]
        for i in range(1, n):
            _gcd = math.gcd(_gcd, nums[i])

        return max(1, math.ceil(nums.count(_gcd)/2))
