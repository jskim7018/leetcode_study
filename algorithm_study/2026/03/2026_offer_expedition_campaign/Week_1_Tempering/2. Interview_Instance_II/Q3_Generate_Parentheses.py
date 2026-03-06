from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: Time complexity = Catalan number
        ans = []

        curr_paren = []
        def backtracking(left: int, right: int):
            if left == 0 and right == 0:
                ans.append(''.join(curr_paren))
                return

            if right > left:
                curr_paren.append(')')
                backtracking(left, right - 1)
                curr_paren.pop()

            if left > 0:
                curr_paren.append('(')
                backtracking(left-1, right)
                curr_paren.pop()
        backtracking(n, n)

        return ans
