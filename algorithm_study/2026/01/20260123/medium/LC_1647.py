from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)

        counter_f = Counter(counter.values())

        stck = list()

        maxim = max(counter_f.keys())
        # TODO stack 없이 frequency 갯수만큼만 loop해서 풀어보자
        ans = 0
        for i in range(1, maxim + 1):
            if i not in counter_f:
                stck.append(i)
            else:
                while counter_f[i] > 1:
                    if stck:
                        empty_place_idx = stck.pop()
                        ans += i - empty_place_idx
                    else:
                        ans += i
                    counter_f[i] -= 1

        return ans
