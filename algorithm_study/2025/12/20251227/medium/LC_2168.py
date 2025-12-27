from collections import defaultdict


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)

        visited = set()
        ans = 0
        for i in range(n):
            counter = defaultdict(lambda: 0)
            _max = 0
            _max_cnt = 0
            for j in range(i, n):
                counter[s[j]] += 1
                if counter[s[j]] > _max:
                    _max = counter[s[j]]
                    _max_cnt = 1
                elif counter[s[j]] == _max:
                    _max_cnt += 1
                if s[i:j+1] in visited:
                    continue

                if _max_cnt == len(counter):
                    ans += 1
                visited.add(s[i:j+1])

        return ans
