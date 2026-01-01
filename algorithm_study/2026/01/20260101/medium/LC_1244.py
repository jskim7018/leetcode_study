from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.player_scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.player_scores:
            self.player_scores[playerId] = score
        else:
            self.player_scores[playerId] += score

    def top(self, K: int) -> int:
        player_scores_list = list(self.player_scores.values())
        player_scores_list.sort()
        _sum = 0
        for i in range(0, K):
            _sum += player_scores_list[-1-i]
        return _sum

    def reset(self, playerId: int) -> None:
        del self.player_scores[playerId]
