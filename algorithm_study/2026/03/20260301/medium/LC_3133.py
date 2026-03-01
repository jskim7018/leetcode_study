import pytest


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # x의 비트 자리 제외하고 나머지 bit에 n의 비트들을 순서대로 배치.

        ans = x
        i = 0
        n -= 1
        while n > 0:
            if ans & (1 << i) > 0:
                i += 1
                continue
            bit = n % 2
            ans |= (bit << i)
            n //= 2
            i += 1

        return ans


@pytest.mark.parametrize("input_n, input_x, expected", [
    (3, 4, 6),
    (2, 7, 15)
])
def test_minEnd(input_n, input_x, expected):
    sol = Solution()

    assert sol.minEnd(input_n, input_x) == expected
