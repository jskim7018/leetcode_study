from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        n = len(s)
        knowledge_dict = {k:v for k,v in knowledge}
        idx = 0
        word = []
        while idx < n:
            if s[idx] == '(':
                idx += 1
                start = idx
                while s[idx] != ')':
                    idx += 1
                end = idx
                key = s[start: end]
                ch = '?'
                if key in knowledge_dict:
                    ch = knowledge_dict[key]
                word.append(ch)
            else:
                word.append(s[idx])
            idx += 1

        return ''.join(word)
