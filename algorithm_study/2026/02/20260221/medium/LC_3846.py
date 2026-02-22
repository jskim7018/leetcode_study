import pytest



class Solution:
    def totalDistance(self, s: str) -> int:
        keyboard = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        ch_to_pos = dict()
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                ch_to_pos[keyboard[i][j]] = (i, j)

        ans = 0
        curr = ch_to_pos['a']
        for ch in s:
            nxt = ch_to_pos[ch]
            ans += abs(curr[0]-nxt[0]) + abs(curr[1]-nxt[1])
            curr = nxt

        return ans


@pytest.mark.parametrize("input_s, expected", [
    ("a", 0),
    ("as", 1),
    ("aqwsa", 4),
    ("hello", 17)
])
def test_totalDistance(input_s, expected):
    sol = Solution()

    assert sol.totalDistance(input_s) == expected
