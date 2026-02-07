from typing import List
from collections import defaultdict
import unittest


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        common_prefix_cnt = defaultdict(int)

        def get_longest_prefix_len(str1: str, str2: str) -> int:
            cnt = 0
            for ch1, ch2 in zip(str1, str2):
                if ch1 == ch2:
                    cnt += 1
                else:
                    break
            return cnt
        n = len(words)
        for i in range(1, n):
            common_prefix_cnt[get_longest_prefix_len(words[i], words[i-1])] += 1

        ans = []
        for i in range(n):
            left = 0
            right = 0
            new = 0
            if i - 1 >= 0:
                left = get_longest_prefix_len(words[i], words[i-1])
                common_prefix_cnt[left] -= 1
                if common_prefix_cnt[left] == 0:
                    del common_prefix_cnt[left]
            if i + 1 < n:
                right = get_longest_prefix_len(words[i], words[i + 1])
                common_prefix_cnt[right] -= 1
                if common_prefix_cnt[right] == 0:
                    del common_prefix_cnt[right]
            if i - 1 >= 0 and i + 1 < n:
                new = get_longest_prefix_len(words[i-1], words[i + 1])
                common_prefix_cnt[new] += 1

            ans.append(max(common_prefix_cnt.keys(), default=0))

            if i - 1 >= 0:
                common_prefix_cnt[left] += 1
            if i + 1 < n:
                common_prefix_cnt[right] += 1
            if i - 1 >= 0 and i + 1 < n:
                common_prefix_cnt[new] -= 1
                if common_prefix_cnt[new] == 0:
                    del common_prefix_cnt[new]

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestCommonPrefix(self):
        actual = self.solution.longestCommonPrefix(["jump","run","run","jump","run"])
        self.assertEqual(actual, [3,0,0,3,3])


if __name__ == '__main__':
    unittest.main()