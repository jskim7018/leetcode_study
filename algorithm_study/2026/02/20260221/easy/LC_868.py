import pytest


class Solution:
    def binaryGap(self, n: int) -> int:

        prev_idx = -1
        idx = 0
        ans = 0
        while n > 0:
            if n % 2 == 1:
                if prev_idx != -1:
                    ans = max(ans, idx-prev_idx)
                prev_idx = idx
            n //= 2
            idx += 1
        return ans

@pytest.mark.parametrize("num, expected", [
    (0,0),
    (1,0),
    (3,1),
    (15,1),
    (17,4)
])
def test_binaryGap(num, expected):
    sol = Solution()
    assert sol.binaryGap(num) == expected