from collections import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            counter = Counter()
            freq_counter = Counter()
            for j in range(i,n):
                if counter[s[j]] != 0:
                    freq_counter[counter[s[j]]] -= 1
                    if freq_counter[counter[s[j]]] == 0:
                        del freq_counter[counter[s[j]]]
                counter[s[j]] += 1
                freq_counter[counter[s[j]]] += 1

                if len(freq_counter) == 1:
                    ans = max(ans, j-i+1)
        return ans
