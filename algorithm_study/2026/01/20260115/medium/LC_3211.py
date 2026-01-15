from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        curr = []

        def dfs(size: int):
            if size == n:
                ans.append(''.join(curr))
                return

            curr.append('1')
            dfs(size + 1)
            curr.pop()

            if not curr or curr[-1] == '1':
                curr.append('0')
                dfs(size + 1)
                curr.pop()
        dfs(0)

        return ans
