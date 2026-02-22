import pytest


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set("aeiou")
        v = 0
        c = 0
        for ch in s:
            if ch in vowels:
                v += 1
            elif ch.isalpha():
                c += 1
        print(f'v: {v}   c: {c}')
        if c > 0:
            return v//c
        else:
            return 0

@pytest.mark.parametrize("s, expected", [
    ("cooear", 2),
    ("axeyizou", 1)
])
def test_vowelConsonantScore(s, expected):
    sol = Solution()
    assert sol.vowelConsonantScore(s) == expected
