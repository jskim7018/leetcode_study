class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)

        ans = list(s)

        i = 0
        while i < n and ans[i] == 'a':
            i += 1

        if i == n:
            ans[n - 1] = 'z'
            return ''.join(ans)

        while i < n:
            if ans[i] != 'a':
                ans[i] = chr(ord(ans[i])-1)
            else:
                if ans[i] == 'a':
                    break
            i += 1

        return ''.join(ans)
