class Solution:
    def canAliceWin(self, n: int) -> bool:
        is_alice_turn = True

        stones_rem = 10
        while True:
            n -= stones_rem
            if n < 0:
                return not is_alice_turn
                break
            stones_rem-=1
            is_alice_turn = not is_alice_turn

        return False
