from typing import List
import math


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        # 제거 효율이 좋은 애들 부터 제거 한다.
        #
        curr_damage = 0
        damage_per_hit = []
        for d, h in zip(damage,health):
            hit_cnt = math.ceil(h/power)
            damage_per_hit.append((d/hit_cnt, d, hit_cnt))
            curr_damage += d

        damage_per_hit.sort(reverse=True)
        ans = 0
        for dph, d, hit in damage_per_hit:
            ans += hit * curr_damage
            curr_damage -= d

        return ans
