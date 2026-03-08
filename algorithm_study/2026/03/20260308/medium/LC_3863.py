import pytest
from collections import defaultdict


class Solution:
    def minOperations(self, s: str) -> int:
        # 정렬을 한거랑 비교.
        # 이미 정렬되어있으면 0
        # 2개면 정렬이 되어있어야 함. 안그러면 -1
        # 여러개 일때 양쪽 끝중 하나라도 되어있으면 정답은 1
        # 양쪽끝 나 안되어있으면 최소 2
        # 만약 양쪽 끝 안되어있으면서 (둘다 freq == 1) 서로 가 교환되어야하면 3
        sorted_s = ''.join(sorted(s))  # 문자열 정렬은 이렇게.

        if sorted_s == s:
            return 0
        elif len(sorted_s) == 2:
            return -1
        elif sorted_s[0] == s[0] or sorted_s[-1] == s[-1]:
            return 1
        else:
            counter = defaultdict(int)
            for ch in s:
                counter[ch] += 1

            if (counter[s[0]] == 1 and s[0] == sorted_s[-1]
                    and counter[s[-1]] == 1 and s[-1] == sorted_s[0]):
                return 3
            else:
                return 2


@pytest.mark.parametrize("input_s, expected", [
    ("dog", 1),
    ("card", 2),
    ("gf", -1),
    ("zbgrda", 3),
    ("zzbgrda", 2),
    ("a", 0),
    ("bazc", 2)
])
def test_minOperations(input_s, expected):
    sol = Solution()

    assert sol.minOperations(input_s) == expected
