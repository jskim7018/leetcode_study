from collections import deque


class Solution:
    def robotWithString(self, s: str) -> str:
        s_with_min = [[c,'z'] for c in s]

        curr_min = 'z'
        for i in range(len(s)-1,-1,-1):
            if s[i] < curr_min:
                curr_min = s[i]
            s_with_min[i][1] = curr_min

        stack = deque()
        ans = []
        for e in s_with_min:
            while stack and stack[-1] <= e[1]:
                ans.append(stack.pop()[0])
            if e[0] <= e[1]:
                ans.append(e[0])
            else:
                stack.append(e[0])

        while stack:
            ans.append(stack.pop()[0])

        return ''.join(ans)
