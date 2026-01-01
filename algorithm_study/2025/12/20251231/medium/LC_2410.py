from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        ans = 0
        t_idx = 0
        for p in players:
            if t_idx >= len(trainers):
                break
            if trainers[t_idx] >= p:
                ans += 1
                t_idx += 1

        return ans
