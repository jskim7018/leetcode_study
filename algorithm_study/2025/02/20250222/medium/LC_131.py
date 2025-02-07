from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def is_palindrome(input: str) -> bool:
            for i in range(len(input)//2):
                if input[i] != input[-i-1]:
                    return False
            return True

        ans = []
        chosen = []
        def dfs(idx):
            nonlocal chosen
            if idx >= n:
                ans.append(list(chosen))
                return

            for i in range(idx, n):
                if is_palindrome(s[idx:i+1]):
                    chosen.append(s[idx:i+1])
                    dfs(i+1)
                    chosen.pop()
        dfs(0)
        return ans
