class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 1e9+7
        ans = 0
        s += '1'

        cnt = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                ans += (cnt*(cnt+1))//2
                ans %= MOD
                cnt = 1
            else:
                cnt += 1

        return int(ans)
