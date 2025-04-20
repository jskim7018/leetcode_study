from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        curr = 0

        ans = 0
        while 0 <= curr < n and instructions[curr] != "":
            new_curr = curr
            if instructions[curr] == 'add':
                ans += values[curr]
                new_curr = curr+1
            else:
                new_curr += values[curr]
            instructions[curr] = ""
            curr = new_curr
        return ans
