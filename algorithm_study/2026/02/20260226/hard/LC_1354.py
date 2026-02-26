from typing import List
import pytest
import heapq
import math


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # arr starts with 1s which means.
        # Each element of array will only keep increasing.
        # Therefore, need to set smallest target first
        # at minimum n-1 will increase.
        # 사실상 특정 element에 자기 자신을 제외한 애들의 모든 합읠 더해주는 것.
        # - 거꾸로 가기? 제일 큰거를 무조건 먼저 다운 시켜야 함. 만약 다른것을 먼저 다운 시키면 음수가 되기 떄문에.
        # 만약 이렇게 해서 모두 1이 된다면 됨. => 왜 이게 가능하지? 앞으로 가는 것과 뒤로가는 것이 어떤 차이가 있길래
        # 앞으로 가는 것은 가능성이 여러개 처럼 느껴지는데 왜 뒤로가는 것은 하나의 길밖이 없지?
        if len(target) == 1:
            if target[0] == 1:
                return True
            else:
                return False
        curr_total_sum = sum(target)
        heap = [-t for t in target]
        heapq.heapify(heap)

        while heap:
            second_best = 1
            maxim = -heapq.heappop(heap)
            if heap:
                second_best = -heap[0]
            curr_total_sum -= maxim
            maxim -= ((maxim-second_best)//curr_total_sum) * curr_total_sum
            if maxim >= second_best and maxim != 1:
                maxim -= curr_total_sum
            curr_total_sum += maxim
            if maxim > 1:
                heapq.heappush(heap, -maxim)  # 1 아니면 다시 넣음.
            elif maxim < 1:
                return False

        return True


@pytest.mark.parametrize("input_target, expected", [
    ([9,3,5], True),
    ([1,1,1,2], False),
    ([8,5], True),
    ([1,1000000000], True),
    ([9,9,9], False)
])
def test_isPossible(input_target, expected):
    sol = Solution()
    assert sol.isPossible(input_target) == expected