from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        n = len(s)

        # TODO: itertools.product 사용하면 편리하게 구현가능. cartesian product
        ans = []
        def dfs(idx: int, word: list):
            if idx >= n:
                ans.append(''.join(word))
                return

            if s[idx] == '{':
                brace_letters = []
                idx += 1
                while s[idx] != '}':
                    if s[idx] != ',':
                        brace_letters.append(s[idx])
                    idx += 1
                brace_letters.sort()
                for ch in brace_letters:
                    word.append(ch)
                    dfs(idx + 1, word)
                    word.pop()
            else:
                word.append(s[idx])
                dfs(idx+1, word)
                word.pop()
        dfs(0, [])

        return ans
