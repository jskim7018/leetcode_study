from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)

        # TODO: 반대로 만족하지 않는 것을 찾고 전체 가능한 경우의 수에서 빼는 방법도 있음.
        counter = defaultdict(int)
        l = 0
        ans = 0
        last_l = 0
        for r in range(n):
            counter[s[r]] += 1
            if counter[s[r]] == k:
                while s[l] != s[r]:
                    counter[s[l]] -= 1
                    l += 1
                ans += max(l+1 - last_l, 1) * (n-r)
                counter[s[l]] -= 1
                l += 1
                last_l = l

        return ans
