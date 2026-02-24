import pytest


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # TODO: You can optimize using:
        # Rolling hash
        # Z-algorithm
        # Suffix array
        n1 = len(word1)
        n2 = len(word2)
        idx1 = 0
        idx2 = 0

        ans = []
        while idx1 < n1 and idx2 < n2:
            if word1[idx1] > word2[idx2]:
                ans.append(word1[idx1])
                idx1 += 1
            elif word1[idx1] < word2[idx2]:
                ans.append(word2[idx2])
                idx2 += 1
            else:
                if word1[idx1:] > word2[idx2:]:
                    ans.append(word1[idx1])
                    idx1 += 1
                else:
                    ans.append(word2[idx2])
                    idx2 += 1

        while idx1 < n1:
            ans.append(word1[idx1])
            idx1 += 1
        while idx2 < n2:
            ans.append(word2[idx2])
            idx2 += 1

        return ''.join(ans)


@pytest.mark.parametrize("input_word1, input_word2, expected", [
    ("cabaa", "bcaaa", "cbcabaaaaa"),
    ("abcabc", "abdcaba", "abdcabcabcaba"),
    ("a", "b", "ba"),
    ("accc", "abbb", "acccabbb"),
    ("abbb", "accc", "acccabbb")
])
def test_largestMerge(input_word1, input_word2, expected):
    sol = Solution()
    assert sol.largestMerge(input_word1, input_word2) == expected
