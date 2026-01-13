from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        def backtrack(idx:int, curr: List[str]):
            if idx >= n:
                ans.append(''.join(curr))
                return

            if s[idx].isalpha():
                curr.append(s[idx].lower())
                backtrack(idx+1, curr)
                curr.pop()

                curr.append(s[idx].upper())
                backtrack(idx + 1, curr)
                curr.pop()
            else:
                curr.append(s[idx])
                backtrack(idx + 1, curr)
                curr.pop()

        backtrack(0, list())

        return ans
