from typing import List
from collections import defaultdict
import pytest


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # TODO: counter로 모두 묶어서 처리 방식도 효율적 (특히 중복 많을때)
        mod = 10**9 + 7
        num_freq = defaultdict(int)
        deliciousness.sort()
        ans = 0
        for d in deliciousness:
            pow_of_two = 1
            for _ in range(22):
                if pow_of_two - d > d:
                    continue
                ans += num_freq[pow_of_two-d]
                ans %= mod
                pow_of_two *= 2
            num_freq[d] += 1

        return ans


@pytest.mark.parametrize("input_deliciousness, expected", [
    ([1,3,5,7,9], 4),
    ([1,1,1,3,3,3,7], 15),
    ([1,1], 1),
    ([1], 0),
    ([1,6], 0),
    ([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234], 12)
])
def test_countPairs(input_deliciousness, expected):
    sol = Solution()
    assert sol.countPairs(input_deliciousness) == expected