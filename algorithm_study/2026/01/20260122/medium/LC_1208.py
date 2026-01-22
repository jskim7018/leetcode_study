class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        l = 0

        curr_cost = 0
        ans = 0
        for r in range(n):
            curr_cost += abs(ord(s[r]) - ord(t[r]))

            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            ans = max(ans, r - l + 1)

        return ans
