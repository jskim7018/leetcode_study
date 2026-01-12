from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)

        total_skill = skill[0] + skill[-1]
        ans = skill[0] * skill[-1]
        for i in range(1, n//2):
            curr_t_skill = skill[i] + skill[-1-i]
            if curr_t_skill == total_skill:
                ans += skill[i] * skill[-1-i]
            else:
                return -1

        return ans
