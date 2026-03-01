import pytest


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last_alph_idx = dict()

        n = len(s)
        ans = []
        curr_actual_idx = 0
        for i in range(n):
            ch = s[i]
            if ch not in last_alph_idx or curr_actual_idx - last_alph_idx[ch] > k:
                ans.append(ch)
                last_alph_idx[ch] = curr_actual_idx
            else:
                curr_actual_idx -= 1
            curr_actual_idx += 1

        return ''.join(ans)


@pytest.mark.parametrize("input_s, input_k, expected", [
    ("abca", 3, "abc"),
    ("aabca", 2, "abca"),
    ("yybyzybz", 2, "ybzybz")
])
def test_mergeCharacters(input_s, input_k, expected):
    sol = Solution()

    assert sol.mergeCharacters(input_s, input_k) == expected
