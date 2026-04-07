class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 아무리 C 레벨에서 수행된다고 해도 4번이나 하는데 이렇게 훨씬 빠를 수가 있나?
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
