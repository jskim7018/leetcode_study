import pytest


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 00 -> 10 or 01.  10 -> 01
        # 2개 있을때 (11이 아닐때 1을 오른쪽의 옮기는 operation)
        n = len(binary)

        zero_cnt = binary.count('0')

        if zero_cnt <= 1:
            return binary

        # TODO: binary.index('0')로 대체 가능
        i = binary.index('0')
        zero_idx = i + (zero_cnt-1)
        ans = ['1'] * n
        ans[zero_idx] = '0'

        return ''.join(ans)


@pytest.mark.parametrize("input_binary, expected", [
    ("000110", "111011"),
    ("01", "01"),
    ("10", "10"),
    ("00", "10"),
    ("111010", "111101"),
    ("011011011", "110111111"),
    ("11", "11")
])
def test_maximumBinaryString(input_binary, expected):
    sol = Solution()
    assert sol.maximumBinaryString(input_binary) == expected
