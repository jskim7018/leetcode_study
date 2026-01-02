class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles

        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            drunk += 1
            empty_bottles += 1
            numExchange += 1

        return drunk
