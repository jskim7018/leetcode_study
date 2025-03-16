from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stck = deque()

        for p in path:
            if p == '..' and stck:
                stck.pop()
            if p == '' or p == '.' or p == '..':
                continue
            stck.append(p)

        return '/' + '/'.join(stck)
