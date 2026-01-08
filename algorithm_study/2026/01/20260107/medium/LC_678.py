class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        visited = [False] * n

        stack = list()

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    idx = stack.pop()
                    visited[idx] = True
                    visited[i] = True

        stack.clear()
        for i, ch in enumerate(s):
            if visited[i]:
                continue
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append('*')

        if not stack or (stack and stack[-1] == '*'):
            return True
        else:
            return False
