from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        curr_time = 0
        bef = [0]*(n+1)
        for j in range(n+1):
            if j == 0:
                bef[j] = curr_time
            else:
                curr_time += skill[j-1] * mana[0]
                bef[j] = curr_time


        to_sub = 0
        curr = [0] * (n + 1)
        for i in range(1, m):
            minim = float('inf')
            for j in range(n+1):
                if j == 0:
                    curr[j] = curr_time
                else:
                    curr_time += skill[j-1] * mana[i]
                    curr[j] = curr_time
                if j < n:
                    time_diff = curr[j] - bef[j + 1]
                    minim = min(minim, time_diff)

            to_sub += minim
            bef = curr

        return bef[n] - to_sub
