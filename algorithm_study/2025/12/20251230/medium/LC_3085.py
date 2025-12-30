from collections import Counter
import bisect


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)

        freq_list = list(counter.values())
        freq_list.sort()

        n = len(freq_list)

        suffix_sum = list(freq_list)
        for i in range(1, n):
            suffix_sum[-1-i] += suffix_sum[-i]

        ans = float('inf')
        left_accum = 0
        for i in range(n):
            idx = bisect.bisect_left(freq_list, freq_list[i] + k + 1)
            curr = left_accum
            if idx < n:
                curr += suffix_sum[idx] - ((freq_list[i] + k) * (n-idx))
            ans = min(ans, curr)
            left_accum += freq_list[i]

        return ans
