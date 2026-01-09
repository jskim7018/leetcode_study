class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_n = len(s)
        t_n = len(t)

        t_idx = 0
        for ch in s:
            if t_idx >= t_n:
                break
            if ch == t[t_idx]:
                t_idx += 1

        ans = t_n - t_idx

        return ans