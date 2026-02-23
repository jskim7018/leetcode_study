import pytest


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        ans = []

        n = len(s)
        count_t_one = t.count('1')

        for i in range(n):
            if n-i == count_t_one:
                if s[i] == '1':
                    ans.append('0')
                else:
                    ans.append('1')
                count_t_one -= 1
            else:
                if count_t_one == 0:
                    ans.append(s[i])
                elif s[i] == '0':
                    count_t_one -= 1
                    ans.append('1')
                else:
                    ans.append('1')

        return ''.join(ans)


@pytest.mark.parametrize("input_s, input_t, expected", [
    ("101", "011", "110"),
    ("0110", "1110", "1101"),
    ("0101", "1001", "1111"),
    ("111000", "010101", "111111"),
    ("1", "1", "0"),
    ("1", "0", "1"),
    ("1110", "1110", "1001")
])
def test_maximumXor(input_s, input_t, expected):
    sol = Solution()
    assert sol.maximumXor(input_s, input_t) == expected
