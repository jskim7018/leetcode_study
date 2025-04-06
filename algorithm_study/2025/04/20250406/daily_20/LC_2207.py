class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        count_0 = 0
        count_1 = 0

        ans = 0
        for c in text:
            if c == pattern[0] and pattern[0] == pattern[1]:
                ans += count_0
                count_0 += 1
                count_1 += 1
            elif c == pattern[0]:
                count_0 += 1
            elif c == pattern[1]:
                count_1 += 1
                ans += count_0

        return ans + max(count_0, count_1)
