class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        n = len(colors)

        for i in range(1,n-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1

        if alice > bob:
            return True
        else:
            return False
