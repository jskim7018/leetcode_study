class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        s += '.'
        n = len(s)

        cnt = 1

        for i in range(1, n):
            if s[i-1] == s[i]:
                cnt += 1
            else:
                if cnt == k:
                    return True
                cnt = 1

        return False
