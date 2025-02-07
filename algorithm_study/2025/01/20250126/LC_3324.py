import string
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []

        curr_input = ""

        alphs = string.ascii_letters
        for c in target:
            idx = ord(c) - ord('a')
            for i in range(idx+1):
                ans.append(curr_input + alphs[i])
                if i == idx:
                    curr_input += alphs[i]

        return ans
