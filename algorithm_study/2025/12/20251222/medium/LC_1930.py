from collections import Counter, defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefix_counter = []

        counter = Counter()

        right_most_alph_idx = defaultdict(lambda: -1)
        for i, ch in enumerate(s):
            counter[ch] += 1
            prefix_counter.append(Counter(counter))
            right_most_alph_idx[ch] = i

        visited = set()
        ans = 0

        for i, ch in enumerate(s):
            if ch in visited:
                continue

            visited.add(ch)

            left_idx = i
            right_idx = right_most_alph_idx[ch]
            middle_cnt = right_idx - left_idx
            if middle_cnt > 0:
                ans += len(prefix_counter[right_idx-1] - prefix_counter[left_idx])

        return ans
