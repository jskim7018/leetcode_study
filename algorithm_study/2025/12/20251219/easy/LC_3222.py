class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        min_playable = min(x, y//4)

        if min_playable % 2 == 1:
            return "Alice"
        else:
            return "Bob"
